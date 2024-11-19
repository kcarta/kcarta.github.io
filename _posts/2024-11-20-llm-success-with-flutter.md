---
layout: post
title:  "Coding LLM Success Case: Flutter"
date:   2024-11-20 00:00:00 +0000
tags: [ai, tools, thoughts]
---

In this post, I intend to show what I consider an ideal case for using an LLM, here ChatGPT, to rapidly generate a working application from scratch. I will call this approach "RAD/LLM" because I am using prompts to an LLM to rapidly iterate, based on what I visually see and want.

The basic cycle is:
- Prompt to generate a starting point
- (Refine by hand as needed)
- View the running application
- Prompt to generate an incremental change
- Immediately view the result (the rapidity at which this and the generation step can be repeated is the crux of this approach)
- (Refine by hand as needed)
- One of the following
  - Prompt to generate a refinement on the latest change
  - Scrap the latest change 
  - Prompt to generate another incremental change
- Repeat until done

In a future dream state, AI reaches a point where it can automate all of the code generation, can do so without need for manual human refinement, and can use any technology to do this.

We are very far from that state.

In practice, today:
- Generated code needs to be applied manually in a programming environment / IDE.
- The manual refinement step is important, as is being able to understand the code that is generated.
- Choice of framework is crucial, as every LLM-based AI I have used will eventually hit show-stopping limitations in *most* frameworks .

In this post, I will show how I carry out the basic RAD/LLM cycle to build relatively-complex apps that actually provide value to use (i.e. aren't simplistic 'toy apps'). I will comment on where I think this cycle works shockingly well, and where I expect future improvements are needed for this to be a generally acceptable approach.

First off, I need to discuss choice of framework, and why I think Flutter is the most ideal framework for this approach.

## Flutter

In my obsessive experimentation since December 2022, I have found Flutter to be an ideal framework for working in a RAD/LLM approach:
- Flutter is a very stable framework, and with some exceptions (mostly in the Dart language), has not changed significantly since its first release in 2017. Apps I wrote in 2018 are still *mostly* valid, and if you showed 2018-me a modern Flutter app, I could have easily understood it.
- Flutter's documentation is comprehensive and easily available, and reasonable to expect is part of any large LLM's training set.
- Flutter and Dart are *simple* to grok, such that anyone who has ever developed a modern mobile or web application can likely read and understand Flutter code without extensive training.
- Flutter's basic architecture is simple: compose (nest) small, simple components (Widgets), and inject services into these as needed.
  - Any small-medium-sized Flutter application found online is likely to follow the same architecture, and this approach is prescribed specifically by the official guidance.
  - This means that an LLM can satisfy a behavior by generating a single Widget in a single file/snippet, instead of needing to correctly generate, for example, a View, Model, and Controller (and Route, and ...).
- Flutter has its own well-documented UI libraries, for Material & Cupertino (Apple native) UI's.
- Flutter's tooling offers 'hot reloading' and 'hot restarting', so (valid) code changes result in immediate UI updates on the development device (i.e. a simulator running next to my IDE).
  - I find this essential for enabling a RAD-like approach.
- Flutter can target Android, iOS, Web, and Desktop, without requiring radically different approaches or split codebases for simple applications.

(Contrast all of these points with SwiftUI, and you'll have a head start to an upcoming post on an LLM Failure Case 😝)

## Case: Building a mail viewer app

The app I want to build is for my personal use: I want to view newsfeed-style all the emails that I've auto-sorted into my "Feeds" mailbox in iCloud Mail.

I think this is an ideal demo of the RAD/LLM approach, as it is complex enough to require UI features like infinite scrolling, calling an external service/API (here, IMAP), caching, etc., but is simple enough that this post won't go on forever and ever.

First off, I can never remember the exact command for `flutter create`, so I use my handy [Ruby script `termgpt`](https://github.com/kcarta/termgpt), which calls the OpenAI API and copies the answer to my clipboard:
``` 
kc@mac ~ % termgpt create new flutter app targetting only ios
flutter create --platforms ios new_flutter_app
kc@mac ~ % cd src
kc@mac src % flutter create --platforms ios mail_feed_reader
Developer identity "Apple Development: Kristofer Carta (********)" selected
for iOS code signing
Creating project mail_feed_reader...
Resolving dependencies in `mail_feed_reader`... 
Downloading packages... 
Got dependencies in `mail_feed_reader`.
Wrote 51 files.

All done!
You can find general documentation for Flutter at: https://docs.flutter.dev/
Detailed API documentation is available at: https://api.flutter.dev/
If you prefer video documentation, consider:
https://www.youtube.com/c/flutterdev

In order to run your application, type:

  $ cd mail_feed_reader
  $ flutter run

Your application code is in mail_feed_reader/lib/main.dart.
```

I open this in my editor, start up my iOS simulator, then start a new session with ChatGPT.

My approach to the starting prompt is:
- Start with context: what is the end goal.
- Describe the core view(s) in the application, and if needed, the basic technical architecture & UI patterns.
- LLM's really like to hallucinate libraries. I typically research libraries ahead of time and name them specifically in the prompt. On occasion I also prompt with how to use them. ChatGPT does especially well with links and at times visits them unprompted.
- End by asking if more input is needed before proceeding. This yields a much higher early success rate than a one-shot prompt (and is, in a simplified manual step, what the new o1-preview model does to itself).

Here, my starting prompt is:

> Let's write a Flutter app together.  
It presents an infinite-scrolling list of expandable and collapsible emails.  
The emails are pulled from an iCloud Mailbox using IMAP, using https://pub.dev/packages/enough_mail  
Email list items are rendered by https://pub.dev/packages/flutter_inappwebview  
Do you have questions before we start?

ChatGPT then responds with:
``` markdown
Got it, this sounds like a fun challenge! Let’s clarify a few points to ensure we're aligned:

Authentication Setup: Do you have an iCloud app-specific password ready to access your mailbox via IMAP? Apple's security is strict, and we'll need an app-specific password for IMAP access.

Email Loading Strategy: Since we’re aiming for infinite scrolling, do you have a preference for:

Loading a fixed number of emails per page (e.g., 20)?

Or should we adapt it based on available screen space?

Email Representation: Using flutter_inappwebview implies that you want emails rendered in HTML. Should we support rich HTML content (like inline images and CSS styles), or should we handle basic text only?

UI/UX Details:
Should the list items show basic details (like sender, subject) when collapsed?
Any specific visuals you’re envisioning for the expandable part, like embedding attachments or images?
Once we confirm these, we can start working on the core architecture and functionality step-by-step.
```

Me:

> I have an iCloud app-specific password ready. This is an app I'm building for personal use so it's fine to just configure this in via an env var or something.  
We should load the latest 20 emails and load more when scrolling down. We should also cache emails so we don't have to keep re-fetching via IMAP.  
flutter_inappwebview does very good rich HTML content formatting, so we will go with that too.  
We'll work on the UI/UX when we get there. A collapsed item shows the subject and sender, and a small snippet of the content. An expanded item shows the full content rendered in rich HTML.

When specifying desired behavior, I am lazier with my RAD/LLM approach than I am at work, where behavior specification is usually the result of extensive design work and will be developed by humans that deserve a clearer explanation of what is intended and why. I have a hunch that LLM's like ChatGPT would excel given a BDD-style prompt, but because I'm choosing to be lazy and good [BDD formulations result from a series of steps](https://bddbooks.com/#formulation), I am leaving this to a future experiment.

ChatGPT now goes off and generates the Flutter project:

- A code snippet with packages that I can place in `pubspec.yaml` (Flutter's main config file) 
- A complete `main.dart` file:
``` dart
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

void main() async {
  await dotenv.load(fileName: ".env");
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Email App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: EmailListScreen(),
    );
  }
}
```
  - ChatGPT chose to include [`flutter_dotenv`](https://pub.dev/packages/flutter_dotenv), which thankfully is also a library I would choose for this little app.
- A service class called `email_service.dart`:
``` dart
import 'package:enough_mail/enough_mail.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

class EmailService {
  static Future<Account> connectToIMAP() async {
    final username = dotenv.env['ICLOUD_USERNAME']!;
    final password = dotenv.env['ICLOUD_PASSWORD']!;
    
    final client = MailClient(
      'imap.mail.me.com',
      isLogEnabled: false,
    );

    await client.connectToServer('imap.mail.me.com', 993, isSecure: true);
    final isLoggedIn = await client.login(username, password);

    if (isLoggedIn) {
      return client.selectInbox();
    } else {
      throw Exception('Failed to login to IMAP');
    }
  }

  static Future<List<MimeMessage>> fetchEmails({int start = 0, int limit = 20}) async {
    final account = await connectToIMAP();
    return await account.fetchMessages(
      count: limit,
      skip: start,
      flags: [FetchFlag.envelope, FetchFlag.body],
    );
  }
}
```

- A StatefulWidget view for the email list:
``` dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'email_service.dart';

class EmailListScreen extends StatefulWidget {
  @override
  _EmailListScreenState createState() => _EmailListScreenState();
}

class _EmailListScreenState extends State<EmailListScreen> {
  List emails = [];
  bool isLoading = false;

  @override
  void initState() {
    super.initState();
    loadInitialEmails();
  }

  Future<void> loadInitialEmails() async {
    setState(() {
      isLoading = true;
    });

    try {
      final loadedEmails = await EmailService.fetchEmails();
      setState(() {
        emails = loadedEmails;
      });
    } catch (e) {
      // Handle error appropriately
    } finally {
      setState(() {
        isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Emails')),
      body: isLoading
          ? Center(child: CircularProgressIndicator())
          : ListView.builder(
              itemCount: emails.length,
              itemBuilder: (context, index) {
                final email = emails[index];
                return ListTile(
                  title: Text(email.envelope.subject ?? 'No Subject'),
                  subtitle: Text(email.envelope.from?.toString() ?? 'Unknown Sender'),
                  onTap: () {
                    // Expand email on tap, yet to implement
                  },
                );
              },
            ),
    );
  }
}

```

ChatGPT concludes with "Next Steps":

``` markdown

## Next Steps

We now have the initial project dependencies, environment setup, and a basic screen that fetches emails from iCloud. Let's continue with:

1. Implement Infinite Scrolling: Use a scroll controller to load more emails as the user scrolls.
2. Add Email Expand/Collapse: Render full content using flutter_inappwebview.
3. Cache Emails: Maintain a cache using provider to minimize redundant IMAP requests.

Do you want me to proceed with infinite scrolling implementation or handle caching next?
```

At this point, because I'm following my RAD/LLM flow, I open my iOS simulator and hit `flutter run`.
