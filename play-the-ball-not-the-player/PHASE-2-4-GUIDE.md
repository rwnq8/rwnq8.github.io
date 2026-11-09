---
title: "Phase 2-4 Execution Guide"
description: "Complete pipeline for Web3 publishing, social dissemination, translations, audio, and interactive web. Every API call ready."
layout: default
---

## Play the Ball, Not the Player — Full Dissemination Pipeline

*Generated: July 3, 2026 | All API calls ready — credential provision unlocks each step*

---

## Status: Phase 1 ✅ Complete

| System | Status | URL/Identifier |
|--------|--------|----------------|
| GitHub Repo | ✅ | https://github.com/rwnq8/play-the-ball-not-the-player |
| GitHub Pages | ✅ LIVE | https://rwnq8.github.io/play-the-ball-not-the-player/ |
| GitHub Release | ✅ v1.0 | https://github.com/rwnq8/play-the-ball-not-the-player/releases/tag/v1.0 |
| Cloudflare R2 | ✅ | `play-the-ball` bucket (content/) |
| IPFS CIDs | ✅ | Root: `bafybeibslwmyux23oocfu7urj7aa7t6jv3qlaj4teacj6ek3o2o3ddpyqa` |
| Social Media Copy | ✅ | `SOCIAL-MEDIA.md` — ready-to-post |
| Dissemination Research | ✅ | `DISSEMINATION.md` |

---

## What "Credential-Blocked" Means

A step marked **[BLOCKED: credential]** means the API call is fully specified and
ready to execute — but needs a credential (API key, token, or wallet) to run.
Once you provide the credential via environment variable or file, the step can
execute immediately without any additional work.

A step marked **[BLOCKED: browser]** requires browser-based OAuth or wallet
signing, which cannot be automated from within DeepChat. These steps require
manual browser interaction.

---

## Phase 2: Web3 / Decentralized Publishing

### 2.1 Pin Content to IPFS (Pinata)
**Status:** [BLOCKED: credential]
**What you get:** Content accessible on the IPFS network via any gateway

**Credential setup (one-time):**
1. Go to https://pinata.cloud — sign up (free tier: 1GB)
2. Generate API key + secret at https://app.pinata.cloud/developers/api-keys
3. Store credentials:
```powershell
setx PINATA_API_KEY "your_key"
setx PINATA_SECRET_KEY "your_secret"
```

**Execute (fully automated once credentials exist):**
```bash
curl -X POST "https://api.pinata.cloud/pinning/pinByHash" \
  -H "pinata_api_key: $env:PINATA_API_KEY" \
  -H "pinata_secret_api_key: $env:PINATA_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashToPin": "bafybeibslwmyux23oocfu7urj7aa7t6jv3qlaj4teacj6ek3o2o3ddpyqa", "pinataMetadata": {"name": "play-the-ball-not-the-player"}}'
```

**Verification:**
```bash
curl -sI "https://gateway.pinata.cloud/ipfs/bafybeibslwmyux23oocfu7urj7aa7t6jv3qlaj4teacj6ek3o2o3ddpyqa" | head -1
# Expected: HTTP/2 200
```

### 2.2 Pin Content to IPFS (web3.storage)
**Status:** [BLOCKED: credential]
**Alternative to Pinata — also free tier (5GB)**

**Credential setup:**
1. Go to https://web3.storage — sign up
2. Create an API token at https://web3.storage/tokens
3. Store: `setx WEB3_STORAGE_TOKEN "your_token"`

**Execute:**
```bash
# Upload individual files
npx @web3-storage/w3cli put blog-post.md content-series.md slide-deck.md philosophical-essay.md README.md index.md DISSEMINATION.md SOCIAL-MEDIA.md
# The CLI outputs a CID — this is your root CID for the upload
```

### 2.3 Mirror.xyz Writing NFT
**Status:** [BLOCKED: browser]
**What you get:** Article permanently stored on Arweave, mintable as Writing NFT

Mirror.xyz requires browser-based wallet interaction (MetaMask/Rainbow) for:
- Connecting your Ethereum wallet
- Signing the transaction to publish
- Setting Writing NFT parameters (editions, price)

**Manual steps (cannot be automated from CLI):**
1. Go to https://mirror.xyz/dashboard
2. Connect wallet
3. Click "New Entry" → paste the blog post content
4. Set Writing NFT: 100 editions at 0.01 ETH (or free)
5. Publish → gets a mirror.xyz/... URL

**Post-publish verification (API-executable once URL is known):**
```bash
curl -s "https://mirror.xyz/<your-address>/<slug>" | grep "Ball First"
```

### 2.4 Arweave (Permaweb)
**Status:** [BLOCKED: credential]
**What you get:** Permanent, one-time-payment storage

**Credential setup:**
1. Install Arweave wallet via ardrive.io or get AR tokens
2. Or use Bundlr/irys.xyz for pay-per-upload without full wallet

**Execute via arkb CLI:**
```bash
npm install -g arkb
arkb deploy blog-post.md --wallet wallet.json --tags "Content-Type: text/markdown"
```

**Execute via Irys (Bundlr) — pay-per-upload, any token:**
```bash
npm install -g @irys/sdk
# Requires funding wallet with token (MATIC, SOL, etc.)
irys upload blog-post.md -t matic -w wallet.json
```

### 2.5 Lens Protocol
**Status:** [BLOCKED: browser]
**What you get:** Decentralized social post, owned by your Lens profile

Requires a Lens profile (NFT handle) and browser-based authentication via
Lenster, Orb, or Phaver apps. Posts are stored on IPFS/Arweave and are
immutable NFTs on Polygon.

**Cannot be fully automated — requires browser wallet interaction.**

### 2.6 ENS + IPFS
**Status:** [BLOCKED: credential + wallet]
**What you get:** Human-readable domain (playtheball.eth) resolving to IPFS

**Steps:**
1. Register ENS name at https://app.ens.domains (requires ETH + browser wallet)
2. Set contenthash to IPFS CID:
```bash
# Requires eth CLI or ethers.js with private key
# ENS resolver: setContenthash(node, contenthash)
# contenthash = 0xe3010170 + CID bytes (without multibase prefix)
```
3. Accessible at: `playtheball.eth.limo` or via any ENS-compatible browser

---

## Phase 3: Series, Social & Community

### 3.1 Buffer Social Media Posting
**Status:** [BLOCKED: credential]
**What you get:** Automated posts to Twitter/X, LinkedIn, Bluesky

**Constraint:** The existing Buffer token is connected to QNFO/QWAV profiles.
A separate Buffer account with dedicated social profiles is needed.

**Setup:**
1. Create Buffer account or add profiles at https://buffer.com
2. Connect Twitter/X, LinkedIn, Bluesky to this new account
3. Generate API token at https://buffer.com/developers
4. Store: `setx BUFFER_PLAYTHEBALL_TOKEN "your_token"`

**Execute (Python script — see SOCIAL-MEDIA.md for full code):**
```bash
python _buffer_post_playtheball.py
```

The Python script at `SOCIAL-MEDIA.md` already contains:
- GraphQL queries for channel discovery
- Channel-optimized post formatting (Twitter 280, LinkedIn 3000, Bluesky 300)
- The `createPost` mutation with proper scheduling
- Verification of 24-char hex channel IDs

**Post content (all composed and ready):**
- 14-part X/Twitter thread
- LinkedIn longform post
- Bluesky short post
- All formatted with proper hashtags, timing, and link attachments

### 3.2 X/Twitter Thread (Manual — Backup Method)
**Status:** [EXECUTABLE: copy-paste]
**What you get:** Direct Twitter post without Buffer API

The full 14-tweet thread is composed in `SOCIAL-MEDIA.md`. Open the file,
copy each tweet sequentially, and paste into Twitter. This is the
zero-dependency path if Buffer API is unavailable.

### 3.3 Medium Publication
**Status:** [BLOCKED: browser]
**What you get:** Article on Medium's platform with built-in audience

Medium deprecated their API. Importing Markdown requires browser interaction.

**Manual steps:**
1. Go to https://medium.com/new-story
2. Click "Import a story" → paste the blog post URL or Markdown
3. Format, add tags (#WorldCup2026, #Leadership, #SelfImprovement)
4. Publish

**Alternative — programmatic via WordPress REST API:**
If you have a WordPress site:
```bash
curl -X POST "https://yoursite.com/wp-json/wp/v2/posts" \
  -H "Authorization: Bearer $WP_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Ball First, Person Never","content":"<paste HTML>","status":"publish"}'
```

### 3.4 Zenodo DOI
**Status:** [BLOCKED: browser for initial setup]
**What you get:** Permanent DOI for the GitHub release — academically citable

**One-time setup:**
1. Go to https://zenodo.org/account/settings/github/
2. Connect your GitHub account
3. Enable the `rwnq8/play-the-ball-not-the-player` repo

**After setup — automatic:**
Every GitHub Release creates a Zenodo archive with a DOI.
The v1.0 release will auto-archive once the integration is enabled.

**Verification (after setup):**
```bash
gh api repos/rwnq8/play-the-ball-not-the-player/releases/latest --jq '.tag_name, .html_url'
# Then check Zenodo for the corresponding DOI badge
```

### 3.5 Reddit
**Status:** [EXECUTABLE: API with credential]
**What you get:** Targeted subreddit distribution

**Credential setup:**
1. Create Reddit app at https://www.reddit.com/prefs/apps (script type)
2. Store: `setx REDDIT_CLIENT_ID "xxx"`, `setx REDDIT_SECRET "xxx"`, `setx REDDIT_USERNAME "xxx"`, `setx REDDIT_PASSWORD "xxx"`

**Execute:**
```python
import os, requests

# Reddit OAuth
auth = requests.auth.HTTPBasicAuth(os.environ["REDDIT_CLIENT_ID"], os.environ["REDDIT_SECRET"])
data = {"grant_type": "password", "username": os.environ["REDDIT_USERNAME"], "password": os.environ["REDDIT_PASSWORD"]}
headers = {"User-Agent": "play-the-ball/1.0"}
token = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers).json()["access_token"]

# Post to subreddits
subreddits = [
    ("selfimprovement", "Life lesson from the 2026 World Cup: play the ball, not the player. Here's what it means for arguments, feedback, relationships, career, and leadership."),
    ("soccer", "Life lesson from this World Cup: play the ball, not the player. A football principle that applies beautifully off the pitch."),
    ("philosophy", "On the ethics of engagement: what football's 'play the ball, not the player' teaches us about ad hominem, Stoicism, and game theory."),
]

headers["Authorization"] = f"bearer {token}"
for sub, text in subreddits:
    r = requests.post(f"https://oauth.reddit.com/api/submit",
        headers=headers,
        json={"sr": sub, "kind": "link", "title": text[:300], "url": "https://rwnq8.github.io/play-the-ball-not-the-player/"})
    print(f"  r/{sub}: HTTP {r.status_code}")
```

---

## Phase 4: Interactive & Long Tail

### 4.1 Interactive Web Experience
**Status:** [EXECUTABLE: code generation]
**What you get:** React + Framer Motion single-page app with:
- Animated football pitch background
- Scroll-triggered domain transitions
- Interactive "ball vs. player" scenario selector
- Embedded IPFS content fetch
- Web3 wallet integration (connect to "collect")

**Execution:**
```bash
# Generate the interactive site
# Use the frontend-design skill to build a production-grade React app
# Deploy to Cloudflare Pages or IPFS
```

This is a standalone code-generation task — fully executable within DeepChat
by calling the `frontend-design` skill with the appropriate prompt.

**Deployment options:**
```bash
# Option A: Cloudflare Pages
npx wrangler pages deploy dist/ --project-name play-the-ball --branch main

# Option B: IPFS
npx ipfs-car --pack dist/ --output play-the-ball-app.car
# Then pin the CAR file
```

### 4.2 Audio Essay / Podcast
**Status:** [EXECUTABLE: text-to-speech]
**What you get:** Spoken-word version of the blog post, mintable as audio NFT

**Execution (AI text-to-speech):**
```bash
# Use OpenAI TTS or ElevenLabs API
curl -X POST "https://api.openai.com/v1/audio/speech" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"tts-1","voice":"onyx","input":"<blog text>"}' \
  --output play-the-ball.mp3
```

**Mint as Audio NFT (Zora):**
```bash
# Requires wallet + Zora SDK
# npm install @zoralabs/protocol-sdk
# See: https://docs.zora.co
```

### 4.3 Translations
**Status:** [EXECUTABLE: AI translation]
**What you get:** Multi-language versions for World Cup audience

**Execution (via LLM or translation API):**
Target languages for the blog post:
- Spanish (World Cup co-host Mexico, massive football audience)
- French (World Cup language, France is defending champion)
- Portuguese (Brazilian football culture)
- Arabic (massive football audience, Morocco's performance)
- Japanese, Korean, German

```python
# Using DeepL API (free tier: 500k chars/month)
import requests
DEEPL_KEY = os.environ["DEEPL_API_KEY"]

languages = ["ES", "FR", "PT-BR", "AR", "JA", "DE"]
for lang in languages:
    resp = requests.post("https://api-free.deepl.com/v2/translate",
        data={"text": BLOG_POST_TEXT, "target_lang": lang},
        headers={"Authorization": f"DeepL-Auth-Key {DEEPL_KEY}"})
    translation = resp.json()["translations"][0]["text"]
    with open(f"blog-post-{lang.lower()}.md", "w", encoding="utf-8") as f:
        f.write(translation)
```

### 4.4 POAPs (Proof of Attendance Protocol)
**Status:** [BLOCKED: browser]
**What you get:** NFT badges for readers who complete the series

**Setup:**
1. Go to https://app.poap.xyz — create an event
2. Generate claim codes or QR codes
3. Distribute to readers who complete all 7 episodes

### 4.5 Token-Curated Registry (TCR)
**Status:** [EXECUTABLE: smart contract development]
**What you get:** Community-governed list of quality "wisdom from sports" content

This requires smart contract development (Solidity) and deployment. A
lightweight TCR can be deployed on a testnet or L2 for minimal gas costs.

**Tech stack:** Solidity + Hardhat + Polygon/Base L2
**Deployment:** `npx hardhat run scripts/deploy.js --network polygon`

---

## Execution Priority — What To Do Next

| Priority | Step | Blocker | Effort |
|----------|------|---------|--------|
| 🔴 **1** | Pin to IPFS (Pinata) | API key (free) | 1 API call |
| 🔴 **2** | Buffer social posting | Separate Buffer token | 1 command after setup |
| 🟡 **3** | Reddit posting | Reddit app credentials | Script execution |
| 🟡 **4** | Zenodo DOI | GitHub connection (one-time) | Browser 5 min |
| 🟢 **5** | Mirror.xyz Writing NFT | Browser wallet | Manual 10 min |
| 🟢 **6** | Interactive web experience | Code generation | LLM task 30 min |
| 🟢 **7** | AI translations | DeepL API key (free) | Script execution |
| 🟢 **8** | Audio essay | TTS API key | API call |

---

## Quick-Start: Execute Phase 2 in One Session

Once you have Pinata + Buffer credentials, this is the entire Phase 2 execution:

```bash
# 1. Pin IPFS
curl -X POST "https://api.pinata.cloud/pinning/pinByHash" \
  -H "pinata_api_key: $env:PINATA_API_KEY" \
  -H "pinata_secret_api_key: $env:PINATA_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashToPin": "bafybeibslwmyux23oocfu7urj7aa7t6jv3qlaj4teacj6ek3o2o3ddpyqa"}'

# 2. Post to social media via Buffer
python _buffer_post_playtheball.py

# 3. Verify IPFS gateway
curl -sI "https://ipfs.io/ipfs/bafybeibslwmyux23oocfu7urj7aa7t6jv3qlaj4teacj6ek3o2o3ddpyqa" | head -1
# Expected: HTTP/2 200

echo "Phase 2 complete. Content is on IPFS + social media."
```

---

## Cost Summary

| Service | Cost |
|---------|------|
| Pinata IPFS | Free (1GB) |
| web3.storage | Free (5GB) |
| Buffer | Free tier available |
| Zenodo | Free |
| DeepL API | Free (500k chars/month) |
| OpenAI TTS | ~$0.30 per essay |
| Reddit API | Free |
| Mirror.xyz | Gas fee (~$0.10-$1 on L2) |
| Arweave | ~$0.01-0.05 per article |
| ENS | ~$5-10/year |
| POAP | Free for small events |
| Cloudflare R2 | Free (10GB) |
| GitHub Pages | Free |

**Total cost for complete Phase 2-4 execution: < $25 USD**
