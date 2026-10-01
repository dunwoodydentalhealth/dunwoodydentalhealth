# Dunwoody Dental Health website
Static HTML/CSS/JS site (Home, About Us, Contact Us).

## Images
Patient photos are in `images/` (patient-1.jpg to patient-6.jpg). Replace a file with the same name to swap a photo.

## Deploy
1. `git init && git add . && git commit -m "Initial site"`
2. Create a GitHub repo, then `git remote add origin <repo-url> && git push -u origin main`
3. Netlify > Add new site > Import from GitHub > pick the repo. Publish directory: `.` (no build command).
4. In `build.py` the `SITE` variable sets canonical URLs, og:image, sitemap.xml and robots.txt. Change it to your real domain, run `python3 build.py`, then commit and push.
The contact form uses Netlify Forms and appears under Forms in the Netlify dashboard after the first deploy.
5. Submit `https://YOURDOMAIN/sitemap.xml` in Google Search Console and Bing Webmaster Tools.
