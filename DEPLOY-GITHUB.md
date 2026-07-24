# Publishing this site on GitHub Pages

The repository is already initialised and committed — it just needs pushing.

## 1. Create the repository on GitHub

Go to <https://github.com/new> and create an **empty** repository (no README,
no .gitignore, no licence — those already exist here).

The name decides the public address:

| Repository name | Site address |
|---|---|
| `xcellence-exim` *(recommended)* | `https://vibhavs12.github.io/xcellence-exim/` |
| `vibhavs12.github.io` | `https://vibhavs12.github.io/` |

Either works. The first keeps your username root free for something else.

## 2. Push

Open Terminal, paste this, and replace `xcellence-exim` if you chose a
different name:

```bash
cd "PASTE_THIS_FOLDER_PATH_HERE"
git remote add origin https://github.com/vibhavs12/xcellence-exim.git
git branch -M main
git push -u origin main
```

To get the folder path: right-click the folder in Finder, hold <kbd>Option</kbd>,
and choose *Copy "…" as Pathname*.

GitHub will ask you to sign in. If it asks for a password, it wants a **personal
access token**, not your account password — create one at
<https://github.com/settings/tokens> with the `repo` scope, and paste that.
(Easier alternative: install [GitHub Desktop](https://desktop.github.com),
drag this folder in, and press Publish.)

## 3. Turn on Pages

In the new repository: **Settings → Pages → Build and deployment**

- Source: **Deploy from a branch**
- Branch: **main**, folder: **/ (root)**
- Save

Give it a minute or two, then reload. Your address appears at the top of that
same Pages screen. Send that link to your friend.

## Updating the site later

```bash
git add -A
git commit -m "Describe what changed"
git push
```

Pages redeploys automatically, usually within a minute.

## Notes

- `.nojekyll` tells GitHub to publish the files exactly as they are rather than
  running them through Jekyll. Leave it in place.
- The `<link rel="canonical">` tags and `sitemap.xml` still point at
  `xcellenceexim.com`. That is deliberate — it stops Google from indexing the
  GitHub preview as a duplicate of the real site. When this becomes the live
  site, change `SITE` at the top of `build/parts.py` and re-run
  `python3 build/build.py`.
- Images currently load from the existing WordPress media library. To make the
  repository fully self-contained, run `bash tools/download-images.sh` followed
  by `bash tools/use-local-images.sh`, then commit the result.
