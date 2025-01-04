---
layout: post
title:  "Shopping (Lists) with Emacs"
date:   2025-01-04 00:00:00 +0000
tags: [emacs]
---

At home, we're tying to re-establish our grocery shopping routine. The cornerstone of this routine is bi-weekly meal planning and shopping - usually on Sundays/Thursdays).

For many years the steps have gone:
1. Open up Notion and go into our shared family workspace
2. Make a new page called something like "Meal Planning Week 2"
3. Do some page setup with a section for each day of the week 
   - At one point we had templates for this, we got lazy and stopped using them
4. Write down what we'll eat on each day
   - We have a recipe bank for inspiration 🤔
5. For each meal planned, list out the items we need to buy in a shopping run
6. (List out anything else we need to get for the week, like detergent)

The end result looks something like this:
![Meal plan in Notion](/static/img/posts/meal-plan-notion.png)

---

Now we have our meal plan written down, the items to go into a shopping list.

For the past year-or-so we've been successfully using a shared "Shopping" list in Apple Reminders. The UX is great and it all works so well when we're in the shop.[^1] [^2] We also have widgets on our phones so we can check the list with some quick gestures.

The irritating part is getting the items into the shopping list. I never found a satisfying way to automate this part 😣[^3] (until now!) .

At an impasse, I gave up, and have been awkwardly copy-pasting the ingredients from Notion over to Apple Reminders - of course this feels *wrong* every time I do it!

On a lucky chance, I came across [this page showing how to invoke AppleScript from Emacs](https://irreal.org/blog/?p=4865) (because of course that's in Emacs!). 

Now, I loathe AppleScript far more than is probably healthy, but sometimes it's the right (i.e. only) tool for the job.

After many iterations and some consultations with my private Emacs tutor, ChatGPT, I was able to scratch together a function that could add an item into my Shopping list:

> Note: if this code can be improved, let me know! I'm still a beginner here and guidance is greatly appreciated.

```elisp
(defun my-add-item-to-shopping-reminders (item)
  "Prompt for ITEM and add it to the ‘Shopping’ list in Apple Reminders."
  (interactive "sAdd item to Shopping: ")
  (let ((as-command (format
	"tell application \"Reminders\"
		tell list \"Shopping\"
			make new reminder with properties {name:\"%s\"}
		end tell
	end tell"
	item)))
    (message "AppleScript: %s" as-command)  ;; Debug
    (shell-command (format "osascript -e '%s'" as-command))))
```

I ended up going with `shell-command` and `osascript` because I couldn't get past permissions blockers between Emacs and Reminders when using `do-applescript` - I really spent a lot of time troubleshooting this before finally giving up 😞

With this milestone reached, I knew there was just one step remaining: get Emacs to process the shopping list items.

With a deal great more iterations and head-scratching, I managed to make a script that:
1. Parses an Org buffer into an AST
2. Gets all the list items from the AST
3. Pushes the content of the list items into a list
4. For each item in the list of content, calls AppleScript to add it to the Apple Reminders "Shopping" list.

> Sidebar: I'm still trying to figure out how I get a good reference for Emacs / library API's. I know I can look things up in Emacs, but if I don't know what to look up, then I have to go online and search around, and if I'm already online, then I don't want to go back to Emacs to complete my reference lookup - a catch-22. This [Org Element API](https://orgmode.org/worg/dev/org-element-api.html) is quite helpful and perhaps an exception to this complaint, but I still wish it were better organized and more detailed. [I'm used to things like this](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/aop/framework/autoproxy/target/AbstractBeanFactoryBasedTargetSourceCreator.html), where even if the subject is ridiculous, it's easy to figure out what I can do with it (if not always why).

The script:
```elisp
(defun my-add-org-items-to-shopping-reminders ()
  "Extract all list items from the current Org buffer and add them to the 'Shopping' list in Apple Reminders."
  (interactive)
  (require 'org-element)
  ;; Extract all list items
  (let ((parsed (org-element-parse-buffer))
        (items '()))
    (org-element-map parsed 'item
      (lambda (item)
        (let ((content (org-element-property :contents-begin item))
              (end (org-element-property :contents-end item)))
          (when (and content end)
            (push (buffer-substring-no-properties content end) items)))))
    ;; Add each item to Apple Reminders
    (dolist (item (reverse items))
      (let ((as-command (format
                         "tell application \"Reminders\"
                            tell list \"Shopping\"
                              make new reminder with properties {name:\"%s\"}
                            end tell
                          end tell"
                         item)))
        (message "Adding to Reminders: %s" item)  ;; Debug
        (shell-command (format "osascript -e '%s'" as-command)))))
  (message "All items added to the 'Shopping' list."))
```

---

Now, I have a new routine:

1. Make the Meal Plan in Notion as usual, with the lists of items we need to get at the store:
![Meal plan in Notion](/static/img/posts/meal-plan-notion.png)

2. Copy-paste the entire Notion page into an Emacs buffer (even \*scratch\* works for this):
![Meal plan in Markdown](/static/img/posts/meal-plan-md.png)

3. Convert Notion's Markdown into Org (not shown: a simple function I have to do this in the same buffer using a shell command to `pandoc`) :
![Meal plan in Org](/static/img/posts/meal-plan-org.png)

4. Run the function to send the list items to Apple Reminders:
![Command to send meal plan items to Apple Reminders](/static/img/posts/meal-plan-command.png)

5. Go shopping!
![Shopping list in Apple Reminders](/static/img/posts/meal-plan-reminders.png)

[^1]: As much as I otherwise love it, Notion has never been 'lightweight' to use on mobile, and is often a real distraction in cases where I *just need* something, like a checklist to quickly reference and update.

[^2]: Also, it's important to keep the meal planning in Notion, because my partner, as smart & wonderful as they otherwise are, is not about to start using some nerdy text editor (😿) or a half-baked app I've written myself (we have enough of those already). Much of our family planning, including our recipes, is also done in Notion.

[^3]: At least one that doesn't require adding an additional service promising to synchronize the two platforms - no thanks!
