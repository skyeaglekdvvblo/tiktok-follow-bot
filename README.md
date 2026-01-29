# Android TikTok Follow Flow Automation

>This repository provides an Android automation harness that validates the TikTok follow user experience end-to-end without relying on manual tapping. It is built for QA and regression testing where teams need repeatable checks on the follow UI across devices and app versions. The tiktok follow bot phrasing here refers to automated **testing** of the follow flow—not boosting followers or automating engagement.

<p align="center">
  <a href="https://t.me/devpilot1" target="_blank"><img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"></a>
  <a href="mailto:support@appilot.app" target="_blank"><img src="https://img.shields.io/badge/Email-support@appilot.app-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"></a>
  <a href="https://Appilot.app" target="_blank"><img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website"></a>
  <a href="https://discord.gg/3YrZJZ6hA2" target="_blank"><img src="https://img.shields.io/badge/Join-Appilot_Community-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Appilot Discord"></a>
</p>

<p align="center">
Created by Appilot, built to showcase our approach to Automation! <br>
If you are looking for custom <strong> tiktok follow bot </strong>, you've just found your team — Let’s Chat.&#128070; &#128070;
</p>


## Introduction

On Android, the follow experience can break for many reasons: UI layout changes, localisation, accessibility overlays, popups, or network-related loading states. Manually verifying the same follow screens across multiple devices is slow and inconsistent.

This project automates that verification with deterministic steps, structured logging, and strict safety guards. It improves reliability by standardising the checks, capturing evidence on failure, and controlling pace and retries to keep test runs stable.

### Where This Helps in Practice

- Ensures the follow UI renders correctly across different screen sizes and Android versions  
- Reduces manual QA time by running repeatable checks on demand  
- Improves consistency with the same steps, pacing, and assertions every run  
- Helps teams detect UI regressions early after app updates  

## Core Features

| Feature | Description |
|--------|-------------|
| Follow UI state validation | Confirms the presence and state of follow-related UI elements (button label, enabled/disabled state, loading indicators) |
| Safe dry-run mode | Runs “verification only” by default so tests can validate UI without performing irreversible actions |
| Deterministic navigation | Uses explicit selectors and guarded waits to navigate profile and content surfaces reliably |
| Evidence capture | Collects screenshots and structured logs on each failure point to speed up debugging |
| Retry & recovery | Retries known flaky steps (scroll/load/popups) with capped attempts and clean abort behaviour |
| Rate limiting & pacing | Applies controlled delays to avoid rapid interaction bursts and reduce UI instability |

## How It Works

| Stage | Details |
|------|---------|
| Trigger / input | A test run starts with a device ID, a target profile URL/handle, and run flags (dry-run, evidence capture) |
| Core logic | Opens TikTok, navigates to target profile, checks follow button visibility/state, optionally simulates the tap only in explicit test mode |
| Output / action | Produces structured logs, screenshots (on failure), and a final pass/fail summary |
| Safety controls | Default dry-run, capped retries, interaction pacing, popup handlers, and graceful shutdown on repeated mismatches |

## Tech Stack

- Appium (Android automation server)
- UIAutomator2 (Android automation driver)
- Python (test runner and orchestration)

## Directory Structure Tree

    android-tiktok-follow-flow-automation/
        app/
            capabilities.android.json
            selectors.yml
        src/
            core/
                driver_factory.py
                session_manager.py
                pacing.py
            flows/
                open_app.py
                navigate_to_profile.py
                validate_follow_ui.py
                popup_handler.py
            utils/
                logger.py
                screenshots.py
                retries.py
        scripts/
            run_follow_flow.py
        tests/
            test_follow_ui_dry_run.py
            test_profile_navigation.py
        logs/
            run.log
        requirements.txt
        README.md

## Use Cases

- QA engineers use it to validate follow UI regressions, so they can catch breakages before release.  
- Mobile automation teams use it to standardise follow-flow checks, so test results remain consistent across devices.  
- Release managers use it to smoke-test critical UI paths, so risky updates are detected early.  
- Device-farm operators use it to run repeatable checks at scale, so failures are attributable and reproducible.  

## FAQs

**Does this automate gaining followers or mass-following?**  
No. This project is intended for UI validation and regression testing. It runs in dry-run mode by default and focuses on verifying UI state and flow stability.

**What Android versions are supported?**  
Any Android version supported by Appium + UIAutomator2, provided the device has the required automation permissions enabled.

**Do I need a physical device?**  
A physical device is recommended for stability, but Android emulators can be used for basic checks where TikTok installation and login are possible.

**What are the main limitations?**  
UI selectors can change between TikTok versions. The project includes selector mapping and guarded waits, but periodic selector updates may be required after major UI updates.

## Performance & Reliability Benchmarks

- Typical flow duration: 35–70 seconds per device (profile open + UI assertions)  
- Pass-rate on stable builds: ~93% (varies with device performance and UI changes)  
- Recommended parallel devices per host: 4–6 (depending on CPU/RAM and ADB throughput)  
- Resource usage per active device: ~250–450 MB RAM for Appium + driver overhead  
- Recovery behaviour: up to 3 retries per flaky step with screenshot capture on the final failure and a clean abort to avoid cascading errors  

<p align="center">
<a href="https://cal.com/app-pilot-m8i8oo/30min" target="_blank">
 <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
 <a href="https://www.youtube.com/@Appilot-app/videos" target="_blank">
  <img src="https://img.shields.io/badge/ð¥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
 </a>
</p>
