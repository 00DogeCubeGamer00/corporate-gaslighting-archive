# Reddit's "Unhelpful Center": An Archive of Automated Gaslighting

This repository serves as a permanent public archive documenting the circular logic, automated containment loops, and systemic failures of modern platform moderation. 

When corporate slogans claim that *"communities are only what we make of them together,"* but build walls of automated scripts to deflect user input, accountability disappears. This project documents what happens when users provide valid critique of a platform's infrastructure, only to be caught in a self-fulfilling enforcement loop.

## The Circular Logic Trap
The enforcement actions taken by the platform demonstrate an irreconcilable, systemic contradiction:
1. The initial warning explicitly states the content was **flagged by automated systems**.
2. The footer of the exact same message claims: **"Note: This decision was made without the assistance of automation."**

Both statements cannot structurally be true. This boilerplate text mimics human accountability to validate arbitrary algorithmic restrictions, effectively weaponizing safety tools to shield corporate support pipelines from critique.

## The Satire Becomes Reality
A parody UI mockup was created to highlight these exact failures, featuring lines like *"Your request was sent to a digital trashmail."* 

During follow-up appeals, this satire was proven to be a direct blueprint of the actual user experience:
- Outbound form requests met severe server timeouts.
- No automated transaction receipts or confirmation emails were dispatched to secure email aliases (like Proton).
- Automated appeal responses completely ignored detailed context, relying strictly on copy-paste verdicts to clear human ticket queues on autopilot.

- ## How to Run the Local Backup Tool

This script utilizes Python and the official PRAW library to extract your personal comment and post histories directly into independent CSV sheets, entirely bypassing the platform's support ticketing queues.

### 1. Prerequisites
Install the required dependencies via your terminal:
```bash
pip install praw
```

### 2. Generate Your Developer API Keys
1. Go to the [Reddit App Preferences](https://reddit.com) panel while logged into your account.
2. Scroll to the bottom and click **"create another app..."**
3. Fill out the fields:
   - **Name:** HistoryBackupTool
   - **App Type:** Select **script**
   - **Redirect URI:** `http://localhost:8080`
4. Click **create app**. 
5. Note the **Client ID** (the random text string underneath the app name) and the **Client Secret** (labeled as "secret").

### 3. Set Variables and Execute
Set your credentials in your terminal session environment so the script can authenticate, then execute the file:

```bash
# On Linux/macOS
export REDDIT_CLIENT_ID="your_client_id"
export REDDIT_CLIENT_SECRET="your_client_secret"
export REDDIT_USERNAME="your_username"
export REDDIT_PASSWORD="your_password"

python backup-script.py
```

## Break the Loop
We do not own the platforms we build on, but we own our data. This repository encourages developers and users to look past restrictive front-facing UIs, deploy local backups, and document structural overreach outside corporate walls.
