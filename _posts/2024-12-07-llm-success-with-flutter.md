---
layout: post
title:  "Rapid LLM app development success case: Flutter"
date:   2024-12-07 00:00:00 +0000
tags: [ai, tools, thoughts]
---

In this post, I intend to show what I consider an ideal case - *with many caveats* - for using an LLM, here ChatGPT, to rapidly generate a working application from scratch. This is a follow-up to my thought-dump on [RAD with LLM's.]({% post_url 2024-11-18-rad-llms %}).

I will call this approach "RAD/LLM" because I am using prompts to an LLM to rapidly develop an application, based primarily on what I visually see and want in the running app.[^1]

To set unrealistically high expectations, here is a scene from Avengers: Endgame that I have been obsessed with ever since I first saw it, and encapsulates my ultimate dream:

<video width="640" preload controls>
	<source src="{{site.baseurl}}/static/img/posts/tony-ai-inspiration.mov" />
</video>

I envision a tight cycle:
- (First time: prompt to generate a starting point)
- **Immediately** view the result
- Then, one of the following:
  - Prompt to generate a refinement on the latest change
  - Prompt to generate a new incremental feature
  - Scrap the latest change 
  - *Manual refinement*
- Repeat until done

**The crux of this approach is the rapidity at which the generate>view>generate steps can be repeated**, while keeping the application running through the steps.[^2]

## The Future, and where we are today

In a future dream state, GenAI tech reaches a point where it can:
- Automate all of the code generation,
- Can do so without need for manual human refinement,
- Can use any technology to do this.

*We are very far from that state.*

As far as I have read and experienced, the modern slate of LLM's fall well short of this (See "[The 70% Problem](https://addyo.substack.com/p/the-70-problem-hard-truths-about)").

In practice, today:
- Generated code needs to be applied manually in a programming environment / IDE that likely never imagined AI code generation as a feature and bolted it on awkwardly,
- The manual refinement step is important, as is being able to understand the code that is generated,
- Choice of framework is crucial, as every LLM-based AI I have used will eventually hit show-stopping limitations in *most* frameworks (as well as going 'vanilla' on a platform).

This post exists in a reality where the RAD/LLM development loop requires programming skill, and expertise with related disciplines like design. Furthermore, what I'm exploring here excludes critical steps like deployment. My cycle does not assume that the LLM will also be generating the things necessary to get an app *production-ready*.[^3]

In this post, I will show how I carry out the basic RAD/LLM cycle to build relatively-complex apps that actually provide value to use (i.e. aren't simplistic 'toy apps'). 

In a follow-up post, I will comment on where I think this cycle works shockingly well, and where I expect future improvements are needed for this to be a generally acceptable approach.

First off, I need to discuss choice of framework, and why I think [Flutter](https://flutter.dev) is an ideal framework for this approach.

## Flutter

In my obsessive experimentation since December 2022, I have found Flutter to be an ideal framework for working in a RAD/LLM approach:
- Flutter is a relatively stable framework.
  - With some exceptions (mostly in the Dart language), it has not changed significantly since its first release in 2017.[^4]
  - **Benefit**: A large LLM's training set has fewer contradictions over framework versions.
- Flutter's documentation is comprehensive and easily available.
  - **Benefit**: It is reasonable to expect that Flutter's docs are part of any large LLM's training set.
- Flutter and Dart are *simple* to grok, such that anyone who has ever developed a modern mobile or web application can likely read and understand Flutter code without extensive training.
  - **Benefit**: Less likely the LLM will hallucinate the basics, and more likely a non-Flutter developer can tweak & shape the generated code.
- Flutter's basic architecture is simple: compose (nest) small, simple components (Widgets), and inject services into these as needed. Larger apps follow MVVM.
  - **Benefit**: Fewer conventions for the LLM to get right.[^5]
  - **Benefit**: Any small-medium-sized Flutter application an LLM might be trained on (e.g. from trawling GitHub) is likely to follow the same architecture, and this approach [is prescribed specifically by the official guidance](https://docs.flutter.dev/app-architecture/recommendations).
- Flutter has its own well-documented UI libraries, for Material & Cupertino (Apple native) UI's.
  - **Benefit**: LLM doesn't also need to know 3rd-party UI libraries.
- Flutter's tooling offers 'hot reloading' and 'hot restarting', so (valid) code changes result in immediate UI updates on the development device (i.e. a simulator running next to my IDE).
  - **Benefit**: Enables the critical step of *immediately seeing the result* of (most) new code.
- Flutter can target Android, iOS, Web, and Desktop, without requiring radically different approaches or split codebases for simple applications.
  - **Benefit**: This approach works on all major platforms.

(Cheeky comment: contrast all of these points with SwiftUI, which changes frequently and has scattershot documentation, and you'll have a head start to an upcoming post on an LLM Failure Case 😝)

## Case: Building a mail viewer app

The app I want to build is for my personal use: 

*I want to view newsfeed-style all the emails that I've auto-sorted into my "[Feed](https://www.hey.com/features/the-feed/)" mailbox in iCloud Mail.*

I think this is an ideal demo of the RAD/LLM approach:
- It is complex enough to require UI features like infinite scrolling, calling an external service/API (here, IMAP), caching, etc.
- It can be built incrementally.
- It is simple enough that I can demo the loop a few times without this post going on forever and ever!

To start: I can never remember the exact command for `flutter create`, so I use my handy [Ruby script `termgpt`](https://github.com/kcarta/termgpt), which calls the OpenAI API and copies the answer to my clipboard.

With the project scaffolded by Flutter, I then open it in my editor, start up my iOS simulator, then start a new session with ChatGPT.

My approach to the starting prompt is usually:
- Start with context: what is the end goal.
- Describe the core view(s) in the application, and if needed, the basic technical architecture & UI patterns.
- LLM's really like to hallucinate libraries. I typically research libraries ahead of time and name them specifically in the prompt. On occasion I also prompt with how to use them.
  - I've never provided full documentation, this has not yet been necessary with Flutter.
- End by asking if more input is needed before proceeding. This yields a much higher early success rate than a one-shot prompt (and is, in a simplified manual step, what the new o1-preview model does to itself).

One final aside: in the rest of this post, I'll blockquote my prompts and put ChatGPT's responses in codeblocks.

My starting prompt (which neglects some of the rules I just outlined 🙃):

> Let's write a Flutter app together.  
It presents an infinite-scrolling list of expandable and collapsible emails.  
The emails are pulled from an iCloud Mailbox using IMAP, using https://pub.dev/packages/enough_mail  
Email list items are rendered by https://pub.dev/packages/flutter_inappwebview  
Do you have questions before we start?

ChatGPT then responds with:
``` markdown
Here are a couple of clarifications before we start:
1. Do you already have the iCloud email setup for IMAP access, including the necessary app-specific password?
2. Are there specific features or UI elements for the email list items you want to include, like swipe actions or particular details?
3. Do you have a preferred state management approach for Flutter in this project (e.g., Provider, BLoC, Riverpod)?
```

Me:

> 1\. Yes  
2\. No   
3\. Provider

When specifying desired behavior and responding to questions, I am lazier with my RAD/LLM approach than I am at work, where behavior specification is usually the result of extensive design work and will be developed by humans that deserve a clearer explanation of what is intended and why. I have a hunch that LLM's like ChatGPT would excel given a BDD-style prompt, but because I'm choosing to be lazy and good [BDD formulations result from a series of steps](https://bddbooks.com/#formulation), I am leaving this to a future experiment.

## Sidebar: an unexpected derailing!

I spent the better part of a year, basically over the GPT-4/turbo lifecycle, working very successfully with this approach.[^6]

I was expecting to be able to recreate it easily for this post.

HOWEVER! I found that both ChatGPT 4o and Claude 3.5 Sonnet were woefully unable to meet the lowest threshold for usable code generation in Flutter. Despite my best efforts, I could not get them to produce anything that didn't produce slews of stupid errors, even sometimes going off the rails on the first simple generation.

For the rest of the post, I fell back to using GPT-4, which worked exactly as well as I had experienced (but unfortunately didn't record comprehensively) earlier this year.

I have no explanation for why GPT-4, which by [all metrics is a less capable model](https://www.vellum.ai/blog/llm-benchmarks-overview-limits-and-model-comparison), works so well with this approach, whereas 4o and Sonnet failed spectacularly. LLM's are weird beasts.

My two hopes for the future of this approach:
1. The incremental "improvements" made with the current leading models represents a "two steps forward, one step back" reality in which my LLM/RAD approach is momentarily not feasible, but where the next generation might inexplicably enable it again.
2. Other leading models - perhaps those trained specifically for code generation - [CodeLamma/Phind](https://www.phind.com/blog/phind-model-beats-gpt4-fast) for example - could perform as well as GPT-4 does. I've used Phind before, but not with this approach. Might be worth further investigation.

## Back to the action

With my first prompt, ChatGPT now goes off and generates the Flutter project:

- Telling me how to create the project.
- A code snippet with packages that I can place in `pubspec.yaml` (Flutter's main config file).
- An EmailProvider class "for handling IMAP connections and fetching emails":
``` dart
import 'package:enough_mail/enough_mail.dart';
import 'package:flutter/material.dart';

class EmailProvider with ChangeNotifier {
  List<MimeMessage> _emails = [];
  bool _isLoading = false;

  List<MimeMessage> get emails => _emails;
  bool get isLoading => _isLoading;

  void fetchEmails() async {
    _isLoading = true;
    notifyListeners();
    
    // Setup IMAP client
    final imapClient = ImapClient(isLogEnabled: false);
    try {
      await imapClient.connectToServer('imap.mail.me.com', 993, isSecure: true);
      await imapClient.login('your-email@icloud.com', 'app-specific-password');
      await imapClient.selectInbox();
      // Fetch recent emails
      final fetchResult = await imapClient.fetchRecentMessages(messageCount: 20, criteria: 'BODY.PEEK[]');
      _emails = fetchResult.messages;
    } catch (e) {
      print('Error fetching emails: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
      imapClient.disconnect();
    }
  }
}
```
- ChatGPT directs me to "Replace 'your-email@icloud.com' and 'app-specific-password' with your actual iCloud email and app-specific password." This isn't good enough, I'll work on it in the next prompt.
- A basic main.dart file:
``` dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'email_provider.dart'; // Assume this is the EmailProvider created earlier

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => EmailProvider()..fetchEmails(),
      child: MaterialApp(
        home: Scaffold(
          appBar: AppBar(title: Text('Infinite Emails')),
          body: Consumer<EmailProvider>(
            builder: (context, provider, _) {
              if (provider.isLoading) {
                return Center(child: CircularProgressIndicator());
              }
              return ListView.builder(
                itemCount: provider.emails.length,
                itemBuilder: (context, index) {
                  final email = provider.emails[index];
                  return ListTile(
                    title: Text(email.decodeSubject() ?? 'No Subject'),
                    subtitle: Text(email.decodeTextPlainPart() ?? 'No Preview'),
                  );
                },
              );
            },
          ),
        ),
      ),
    );
  }
}
```

``` markdown
"We'll use a `ListView.builder` for infinite scrolling and a `Provider` to manage state. Here's a simple UI setup in your `main.dart`"

This is a basic setup. We can add more features like error handling, pull-to-refresh, and expandable list items using ExpansionTile. Let me know how you'd like to proceed or if you have any adjustments!
```

**Pitfall**: the packages ChatGPT gave me were out of date. It's very unlikely that any LLM will have the latest versions, so it's necessary to make sure these are valid & updated by hand. Sometimes I'll provide the ideal packages with their versions in the starting prompt, if I know them already.

At this point, because I'm following my RAD/LLM flow, I hit `flutter run` and see the first result on my iOS Simulator:

![First generation with Flutter & ChatGPT 4](/static/img/posts/flutter_llm_gen1.png)

Not too bad! No error messages, the content loads quickly and correctly, and with nice-to-haves like a loading spinner. For a first round, and a few minutes' work, I already have something I could call a rough proof-of-concept, if still short of a usable prototype.

Satisfied with this result, I continue:

> This worked!  
Let's proceed in the following steps:  
1\. Improve the Email Provider to read login information and desired mailbox (not the inbox) from a .env file (use flutter_dotenv 5.2.1)  
2\. Styling the list items, including expansion  
3\. Pull-to-refresh, infinite scrolling, and caching  
Sound good? Any questions?  
If no questions, we can proceed to 1.  
The variables I want to store are:  
EMAIL  
PASSWORD  
MAILBOX  
MAILBOX_PATH  
You might have outdated knowledge of flutter_dotenv. It can now be used inline like: dotenv.env['KEY']. Let's just load the variables inline, defaulting to 'INBOX' for MAILBOX and MAILBOX_PATH, and throw an error if EMAIL or PASSWORD are null. 

---

GPT-4 has outdated information about flutter_dotenv, so after a failed generation, I rewrote the prompt to supply the additional context, including for the variables I wanted to store (I probably didn't need to do this, though). Examples like this are why it's necessary to have *some* framework knowledge in order to follow this approach. As long as the LLM is doing most of the work, and we're progressing forward quickly, I'm happy.

ChatGPT responded by reiterating my prompt, then directing me to add a dependency to my `pubspec.yaml` file and create a `.env` file (I won't paste these here, it's what you'd expect):

``` markdown
Sounds like a good plan! Let’s break it down step by step, starting with step 1.

## Step 1: Integrate `flutter_dotenv` for Environment Variables

First, you'll need to add `flutter_dotenv` to your `pubspec.yaml` and load the .env variables in your email provider.

...
```

It then directs me to "Modify `EmailProvider` to use `flutter_dotenv`"

ChatGPT generated the full class again (fine with me, easier to copy-paste), I'll just show the snippet that changed, in the `fetchEmails` method:

``` dart
   // Load environment variables
    await dotenv.load();
    final email = dotenv.env['EMAIL']!;
    final password = dotenv.env['PASSWORD']!;
    final mailbox = dotenv.env['MAILBOX'] ?? 'INBOX';
    final mailboxPath = dotenv.env['MAILBOX_PATH'] ?? mailbox;

    if (email == null || password == null) {
      throw Exception('Email and password must not be null');
    }

    // Setup IMAP client
    final imapClient = ImapClient(isLogEnabled: false);
    try {
      await imapClient.connectToServer('imap.mail.me.com', 993, isSecure: true);
      await imapClient.login(email, password);
      await imapClient.selectMailboxByPath(mailboxPath);
```

```
This setup introduces inline loading of environment variables and makes use of them in the email fetching logic.

Now that the Email Provider is updated to handle .env configurations and custom mailbox paths, we can proceed to Step 2: Styling the list items, including expansion. Let me know if you're ready to move on or if there's anything else from Step 1 to adjust!
``` 

I like that we're both asking each other if we're ready before proceeding.

I encountered a small error, that I quickly fixed:[^7] 

> Small error fix: I changed email and password to default to an empty string and changed the check on email and password to be .isEmpty(), now this works.  
Let's move onto the styling for the list items.  
Each list item should have a header containing the sender, subject, and date, and a snippet for a content preview. It's probably a good idea to make a widget for the list items.

ChatGPT:

``` markdown
Excellent! Let's design a widget for the list items that includes a header with the sender, subject, and date, as well as a snippet for the content preview. We'll use ExpansionTile for the expandable/collapsible functionality. This approach will provide a clean, organized display for your emails.

## Step 2: Styling List Items with a Custom Widget

### Creating a Custom List Item Widget

We'll define a custom widget named EmailListItem that takes a MimeMessage and displays the necessary details. Here's a possible implementation:

```

``` dart
import 'package:flutter/material.dart';
import 'package:intl/intl.dart'; // Add this to your pubspec.yaml for date formatting
import 'package:enough_mail/enough_mail.dart';

class EmailListItem extends StatelessWidget {
  final MimeMessage email;

  EmailListItem({required this.email});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ExpansionTile(
        title: _buildTitle(email),
        subtitle: Text(
          email.decodeTextPlainPart()?.split('\n').first ?? 'No content preview',
          maxLines: 2,
          overflow: TextOverflow.ellipsis,
        ),
        children: [
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Text(email.decodeTextPlainPart() ?? 'No content available'),
          ),
        ],
      ),
    );
  }

  Widget _buildTitle(MimeMessage email) {
    return Row(
      children: [
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                email.from?.first.email ?? 'Unknown sender',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
              Text(
                email.decodeSubject() ?? 'No subject',
                style: TextStyle(color: Colors.grey[600]),
              ),
            ],
          ),
        ),
        Text(
          DateFormat('MMM dd, yyyy').format(email.decodeDate() ?? DateTime.now()),
          style: TextStyle(color: Colors.grey[600]),
        ),
      ],
    );
  }
}
``` 
``` markdown
### Update Your Main UI

Now, replace the ListTile in your ListView.builder in main.dart with the new EmailListItem widget:
``` 
``` dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'email_provider.dart'; // Assume this is the EmailProvider created earlier
import 'email_list_item.dart'; // The custom widget we just created

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => EmailProvider()..fetchEmails(),
      child: MaterialApp(
        home: Scaffold(
          appBar: AppBar(title: Text('Infinite Emails')),
          body: Consumer<EmailProvider>(
            builder: (context, provider, _) {
              if (provider.isLoading) {
                return Center(child: CircularProgressIndicator());
              }
              return ListView.builder(
                itemCount: provider.emails.length,
                itemBuilder: (context, index) {
                  final email = provider.emails[index];
                  return EmailListItem(email: email);
                },
              );
            },
          ),
        ),
      ),
    );
  }
}
``` 
``` markdown
This setup includes a more structured and visually appealing email list item with collapsible content. If this meets your expectations, we can move on to implementing pull-to-refresh, infinite scrolling, and caching next. Let me know if you'd like any adjustments to the styling or additional features before we proceed!
```

The result, now after about 5 minutes since we started (excluding time spent documenting for this post 😉):

![Flutter LLM-generated app, round 2](/static/img/posts/flutter_llm_gen2.png)

Selecting any list item expands to show the full content, but just in text. I want the rendered HTML, since most of the emails coming into my 'Feed' folder have rich content.

Next, I want ChatGPT to render the HTML content in the expanded emails.

After a failed generation, where it turned out ChatGPT didn't know how to use `flutter_inappwebview` despite doing so correctly in a previous project (🤷🏻‍♂️). I spent a minute referring to the docs and copying a snippet from the previous project. Also, I realized my initial prompt didn't narrow down to just targeting iOS, so I mention that now (oops!).

> This worked! For the expanded content, let's use flutter_inappwebview to render the HTML content.   
Here is an example of using an InAppWebView widget as a child of a SizedBox. The content is the raw HTML from the email.  
`CODE_SNIPPET`  
Finally, note that I'm only building this for iOS currently.

ChatGPT:

``` markdown
Perfect! Let’s integrate the `InAppWebView` to render the HTML content of the emails when they are expanded. You've provided a good example of how to configure the widget. Let's adapt this to the `EmailListItem` widget.

## Integrating `flutter_inappwebview` for HTML Content Rendering
We'll modify the `EmailListItem` widget to include the InAppWebView for displaying HTML content in the expansion panel.

### Update the `EmailListItem` Widget

Here's the updated `EmailListItem` widget including `InAppWebView` for rendering HTML content:
```
``` dart
import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:enough_mail/enough_mail.dart';
import 'package:flutter_inappwebview/flutter_inappwebview.dart';

class EmailListItem extends StatelessWidget {
  final MimeMessage email;

  EmailListItem({required this.email});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ExpansionTile(
        title: _buildTitle(email),
        subtitle: Text(
          email.decodeTextPlainPart()?.split('\n').first ?? 'No content preview',
          maxLines: 2,
          overflow: TextOverflow.ellipsis,
        ),
        children: [
          SizedBox(
            height: 300, // Adjust the height as needed
            child: InAppWebView(
              gestureRecognizers: {
                Factory<OneSequenceGestureRecognizer>(
                  () => VerticalDragGestureRecognizer(),
                ),
              },
              initialData: InAppWebViewInitialData(
                data: email.textHtmlPart ?? '<p>No HTML content available</p>',
              ),
              initialSettings: InAppWebViewSettings(
                verticalScrollBarEnabled: true,
                horizontalScrollBarEnabled: false,
                scrollBarStyle: ScrollBarStyle.SCROLLBARS_INSIDE_INSET,
                supportZoom: false,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildTitle(MimeMessage email) {
    return Row(
      children: [
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                email.from?.first.email ?? 'Unknown sender',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
              Text(
                email.decodeSubject() ?? 'No subject',
                style: TextStyle(color: Colors.grey[600]),
              ),
            ],
          ),
        ),
        Text(
          DateFormat('MMM dd, yyyy').format(email.decodeDate() ?? DateTime.now()),
          style: TextStyle(color: Colors.grey[600]),
        ),
      ],
    );
  }
}
```
``` markdown
In this setup, the `InAppWebView` is wrapped within a `SizedBox` to control its height, ensuring it doesn’t expand indefinitely within the `ExpansionTile`.
```

I copy-paste the code, make a few fixes, and hot reload the app. The content is now fully-rendered:

![Third generation with Flutter and ChatGPT 4](/static/img/posts/flutter_llm_gen3.png)

I needed to make a few tweaks:

- Missing package imports
- `textHtmlPart` was not a getter on `MimeMessage`, ChatGPT hallucinated this. The fix was easy, just finding and using the method `decodeTextHtmlPart`.

These tweaks took under a minute.

## A fine stopping point: conclusions

Having done three rounds of generation, I have, in a little over five real-time minutes,[^8] gone from an idea to a fully-working prototype that I can see, use, and easily iterate on.

Thanks to Flutter's hot reload & restart, most changes were visible in the running application immediately after I pasted (and patched) the generated code. At worst, I had to redeploy, which takes a handful of seconds, mostly waiting on Xcode build (so, I'd assume the redeploy is faster on any other platform...).

This approach, where I facilitate and ChatGPT does the vast majority of the actual work, with some gentle prodding, is not *really* my 'endgame', *yet* - but it does feel absolutely **exhilarating** to be able to take an idea to working software so effectively.[^9]

What this feels like to me, is that I've used **cheat codes** to skip past all the boring boilerplate and frameworking I usually have to slog through, and that I don't care about when I'm just trying to get a working prototype on an idea. *If I had a nickel for every project that I never finished because I ended up sinking into the swamp of initial boilerplate and framework-wrangling... 😵*

Of course, there's still much to do, to get this app polished and delightful to use, like:

- Fixing the weird icon used to show collapsed/expanded state
- Tweaking the styling and layout of the various header & title elements
- Implementing fetching of additional emails (infinite scrolling), fetching new emails, and caching

Having built a similar app using this same approach, but fetching from Gmail and using Firebase for auth, I know these are feasible within a reasonably quick time frame.

I plan to write a follow-up post soon showing the final result and how long it took me to reach that state following my RAD/LLM approach.

On the code side, around this point I'll usually spend a few minutes reading in detail through all the code, so I understand more-or-less what's going on in the whole solution. Maybe I'll also do some refactoring or clean-up, but usually not too much.

If I make any code changes, then I'll share the latest code in snippets to ChatGPT before the next round of generation.

Sometimes, to make sure ChatGPT is using only valid context, I'll start a new chat, with a first prompt that gives an overview of the application, the purpose, and then the code (or an outline with snippets if there is too much code to share). Sometimes I find this keeps the quality of the generations higher than if I stay in the same chat. This approach, in classic Wild Wild West style, is more about gut feeling and inexplicable steampunk magic than documentable, replicable science 🙃

## Parting thoughts

I hope this demo has convinced you that it can be possible now for a single developer to quickly iterate and build an application of value (or at least a prototype of value), using the right tools, approach, and framework. 

What I think differentiates this approach to others I've seen, is that I'm using off-the-shelf tools, not a specialized environment tailored specifically to AI-generating an application.

I have always considered myself a relatively slow (methodical?) developer, so for me, this approach gives me a time boost at least an order of magnitude above what I could do if I were to write the application from scratch manually - a true game-changer and something approaching the advertised promise of these GenAI/LLM tools.

For a taste of a larger application I built entirely with this RAD/LLM approach, see my [flash-cards-ru](https://github.com/kcarta/flash-cards-ru) repo. This approach let me rapidly build a rich application with native iOS look & feel and of a size & complexity that I would never have attempted otherwise. I also used GPT-4 to generate all of the vocabulary files and grammar rules, also something I would never have been able to do in a reasonable time-frame myself.

[^1]: I don't know if this is already called something. AI-assisted develoment is where we are now, but this falls short of my dream, I think. As a developer, I want to assist the AI, not the other way around.

[^2]: Note that the flow works very well with BDD/TDD, maybe even [TCR](https://medium.com/@kentbeck_7670/test-commit-revert-870bbd756864)? I'd like to experiment and demo these approaches next.

[^3]: I expect tooling/services will saturate the market *soon (some exist already) that will close the loop between generation and deployment. I would hesitate to use these with anything requiring any level of security (although I have made some useful apps with Firebase auth that could be releasable).

[^4]: Flutter apps I wrote in 2018 are still *mostly* valid, and if you showed 2018-me a modern Flutter app, I could have easily understood it. 

[^5]: For this reason, I found working with Rails, as much as I love it, to be very error-prone after the first round or so of code generation. Rails is anyways so productive for an experienced developer that I reckon the time savings would be minimal using AI.

[^6]: 'Very successsfuly' meaning that the LLM generates >90% of the code successfully, and I edit the rest or nudge the LLM with re-prompting. Any less than 90% makes this approach infeasible.

[^7]: I forgot to mention, ChatGPT forgot to have me add the `.env` file as an asset in `pubspec.yaml`

[^8]: Granted, some things made it faster for me to do this, like having a code snippet for the HTML rendering. However, this isn't a showstopper and anyways takes as much or less time as learning and implementing the same behavior manually.

[^9]: Especially when I'm working with a framework like Flutter that I'm not a professional with, that is, I'm not hacking with it day in and day out and so not coding at ninja-speed whenever I want to play with an idea.
