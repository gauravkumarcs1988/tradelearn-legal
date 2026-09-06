"""Generate the static legal/support pages for GitHub Pages.

    python build_pages.py

Plain HTML, no external assets, light + dark. Re-run after editing the copy.
Published at https://gauravkumarcs1988.github.io/tradelearn-legal/
"""

from __future__ import annotations

import pathlib

OUT = pathlib.Path(__file__).resolve().parent

STYLE = """
  :root { color-scheme: light dark; }
  * { box-sizing: border-box; }
  body { margin:0; padding:0; font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif; color:#0F172A; background:#F8FAFC; }
  header { background:#0E1B2A; color:#fff; padding:40px 24px; }
  header .wrap { max-width:760px; margin:0 auto; }
  header h1 { margin:0 0 6px; font-size:28px; letter-spacing:-.5px; }
  header p { margin:0; color:#93B4E8; font-size:14px; }
  main { max-width:760px; margin:0 auto; padding:32px 24px 72px; }
  h2 { font-size:20px; margin:34px 0 10px; letter-spacing:-.3px; }
  h3 { font-size:16px; margin:22px 0 8px; }
  p, li { color:#334155; }
  ul { padding-left:22px; } li { margin:6px 0; }
  table { width:100%; border-collapse:collapse; margin:14px 0; font-size:15px; }
  th, td { text-align:left; padding:10px 12px; border-bottom:1px solid #E2E8F0; vertical-align:top; }
  th { background:#F1F5F9; font-weight:600; }
  code { background:#F1F5F9; padding:1px 5px; border-radius:4px; font-size:14px; }
  .box { background:#EFF5FF; border-left:3px solid #4080FF; padding:14px 16px; border-radius:8px; margin:18px 0; }
  .warn { background:#FFF4E5; border-left:3px solid #E08700; padding:14px 16px; border-radius:8px; margin:18px 0; }
  .card { display:block; background:#fff; border:1px solid #E2E8F0; border-radius:12px; padding:18px 20px; margin:12px 0; text-decoration:none; }
  .card strong { display:block; color:#0F172A; font-size:17px; margin-bottom:3px; }
  .card span { color:#64748B; font-size:14px; }
  a { color:#1D4ED8; }
  footer { border-top:1px solid #E2E8F0; margin-top:40px; padding-top:18px; font-size:13px; color:#64748B; }
  @media (prefers-color-scheme: dark) {
    body { background:#0F172A; color:#F1F5F9; } p,li { color:#CBD5E1; }
    th { background:#1E293B; } th,td { border-bottom-color:#1E293B; }
    code { background:#1E293B; }
    .box { background:rgba(64,128,255,.15); }
    .warn { background:rgba(224,135,0,.15); }
    .card { background:#1E293B; border-color:#334155; } .card strong { color:#F1F5F9; }
    a { color:#93B4E8; } footer { border-top-color:#1E293B; }
  }
"""

FOOTER = """
  <footer>Trade Learn &middot; <a href="./index.html">All policies</a> &middot;
  <a href="./privacy-policy.html">Privacy</a> &middot;
  <a href="./terms.html">Terms</a> &middot;
  <a href="./account-deletion.html">Delete my data</a> &middot;
  <a href="./support.html">Support</a></footer>
"""

CONTACT_EMAIL = "gauravkumar.cs1988@gmail.com"
CONTACT_PHONE = "+91 84478 85185"
PACKAGE = "com.tradelearn.app"
UPDATED = "7 September 2026"


def page(filename: str, title: str, subtitle: str, body: str) -> None:
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} &mdash; Trade Learn</title>
<meta name="description" content="{title} for Trade Learn, the paper-trading practice app.">
<style>{STYLE}</style>
</head>
<body>
<header><div class="wrap"><h1>{title}</h1><p>Trade Learn &middot; {subtitle}</p></div></header>
<main>
{body}
{FOOTER}
</main>
</body>
</html>
"""
    (OUT / filename).write_text(html, encoding="utf-8")
    print(f"  {filename}")


page(
    "index.html",
    "Trade Learn",
    "Policies and support",
    """
  <p>Trade Learn is a practice app for learning to trade Indian markets. Every position is
     simulated on live market data &mdash; no order is ever placed with a broker and no real
     money is ever at risk.</p>

  <a class="card" href="./privacy-policy.html"><strong>Privacy Policy</strong>
     <span>What we collect, why, and how it is protected.</span></a>
  <a class="card" href="./terms.html"><strong>Terms of Service</strong>
     <span>The agreement covering your use of the app.</span></a>
  <a class="card" href="./account-deletion.html"><strong>Delete your account and data</strong>
     <span>How to permanently remove everything.</span></a>
  <a class="card" href="./support.html"><strong>Support</strong>
     <span>Get help by email or WhatsApp.</span></a>
""",
)

page(
    "privacy-policy.html",
    "Privacy Policy",
    f"Last updated {UPDATED}",
    f"""
  <p>
    Trade Learn is a paper-trading practice app. This policy explains what we collect, why, and
    what control you have. It applies to the Android app (<code>{PACKAGE}</code>) and its backend
    service.
  </p>

  <div class="box">
    <strong>The short version.</strong> You sign in with Google, and we ask for your mobile number
    so we can identify your account. We store the practice trades you make. We do not sell your
    data, we do not show ads, and we never see your card or UPI details.
  </div>

  <h2>1. Who we are</h2>
  <p>
    Trade Learn is operated by the app publisher listed on the Google Play store page.
    For any privacy question, contact
    <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.
  </p>

  <h2>2. What we collect</h2>
  <table>
    <tr><th>Data</th><th>Why we need it</th></tr>
    <tr>
      <td><strong>Google account details</strong></td>
      <td>
        Your email address, display name, profile picture and Google account identifier, received
        when you choose &ldquo;Continue with Google&rdquo;. This is how your account is created and
        recognised on your next sign-in. We never receive your Google password.
      </td>
    </tr>
    <tr>
      <td><strong>Mobile number</strong></td>
      <td>
        Collected once, right after sign-up. It identifies your account uniquely and is how we
        reach you about your subscription. One number, one account.
      </td>
    </tr>
    <tr>
      <td><strong>City and experience level</strong></td>
      <td>Optional. Used to understand who is using the app and to pitch the content sensibly.</td>
    </tr>
    <tr>
      <td><strong>Your practice trades</strong></td>
      <td>
        The simulated positions you open and close, your watchlist, and your practice portfolio
        balance. This is the content of the app &mdash; it exists because you created it.
      </td>
    </tr>
    <tr>
      <td><strong>Payment records</strong></td>
      <td>
        If you buy access: the order and payment reference, the amount, the number of days, and
        the date. Handled by Razorpay &mdash; see section 5.
      </td>
    </tr>
    <tr>
      <td><strong>Device and app information</strong></td>
      <td>
        Device name, Android version and app version. Used to keep your session on the right
        device and to diagnose faults.
      </td>
    </tr>
    <tr>
      <td><strong>Technical logs</strong></td>
      <td>IP address and request timestamps, kept briefly for security and abuse prevention.</td>
    </tr>
  </table>

  <h3>What we do <em>not</em> collect</h3>
  <ul>
    <li>No location data. The app does not request location permission.</li>
    <li>No contacts, photos, files, microphone or camera access.</li>
    <li>No advertising identifiers. There are no ads and no ad networks in this app.</li>
    <li>No third-party analytics or tracking SDKs.</li>
    <li>No demat account, broker credentials or bank details. The app cannot place real trades.</li>
    <li>We never see or store your card, UPI or netbanking credentials.</li>
  </ul>

  <h2>3. How we use your data</h2>
  <ul>
    <li>To create and secure your account, and to keep you signed in.</li>
    <li>To store and show back the practice trades and watchlists you create.</li>
    <li>To work out whether your free trial or paid access is still running.</li>
    <li>To take payment for access and keep a record of it.</li>
    <li>To detect and prevent abuse, fraud and technical faults.</li>
  </ul>
  <p>
    We do <strong>not</strong> use your data to build advertising profiles, and we do not sell or
    rent your personal data to anyone.
  </p>

  <h2>4. Separation between users</h2>
  <p>
    Each account's data is isolated. You cannot see another user's trades, watchlist or portfolio,
    and they cannot see yours. The app owner can see account and usage information for support and
    billing purposes, described in section 8.
  </p>

  <h2>5. Who your data is shared with</h2>
  <p>We share data only with the service providers needed to run the app:</p>
  <table>
    <tr><th>Provider</th><th>What they receive</th><th>Purpose</th></tr>
    <tr>
      <td><strong>Google</strong> (Sign-In, Play)</td>
      <td>Your sign-in request. We receive your email, name and picture back.</td>
      <td>Authentication and app distribution.</td>
    </tr>
    <tr>
      <td><strong>Razorpay</strong></td>
      <td>Your name, email and mobile number, and the amount, when you make a payment.</td>
      <td>
        Processing payments. Card, UPI and netbanking details are entered on Razorpay's own
        screen and never reach us. Razorpay is an RBI-authorised payment aggregator.
      </td>
    </tr>
    <tr>
      <td><strong>Upstox</strong></td>
      <td>Nothing about you.</td>
      <td>
        Live market prices, candles and option chains. We hold one broker connection for the whole
        service; no personal data is sent, and no account of yours is involved.
      </td>
    </tr>
    <tr>
      <td><strong>Google Gemini</strong> and <strong>Anthropic Claude</strong></td>
      <td>Market price data only &mdash; no personal data, ever.</td>
      <td>
        Two of the three engines that score a trade setup. They receive candles and indicator
        values for a stock or index. They are never sent your name, email, phone or trades.
      </td>
    </tr>
    <tr>
      <td><strong>Amazon Web Services</strong></td>
      <td>Everything, at rest, in the Mumbai region.</td>
      <td>Hosting the backend and database.</td>
    </tr>
  </table>
  <p>
    We also disclose data where the law requires it, or to protect our rights or the safety of
    others.
  </p>

  <h2>6. Where your data is stored</h2>
  <p>
    On servers in India (AWS Asia Pacific, Mumbai). Traffic between the app and the server is
    encrypted with HTTPS. Sign-in tokens are held in the Android Keystore on your device.
  </p>

  <h2>7. How long we keep it</h2>
  <ul>
    <li><strong>Account and trades</strong> &mdash; while your account exists. Delete the account
        and they go with it.</li>
    <li><strong>Payment records</strong> &mdash; retained for as long as tax and accounting law
        requires, even after the account is closed. Not used for any other purpose.</li>
    <li><strong>Technical logs</strong> &mdash; a few days, then discarded automatically.</li>
  </ul>

  <h2>8. What the app owner can see</h2>
  <p>
    Trade Learn has a single owner account used to run the service. It can see the list of
    registered users, each account's name, email, mobile number, subscription state and payment
    history, when each user was last active, and the practice trades currently open. This is for
    support, billing and abuse prevention. It is not shared with anyone else.
  </p>

  <h2>9. Your rights and choices</h2>
  <ul>
    <li><strong>Access and correction</strong> &mdash; your details are on the Account screen, and
        you can ask us for a copy of anything else we hold.</li>
    <li><strong>Deletion</strong> &mdash; delete your account from inside the app, on the Account
        screen. See <a href="./account-deletion.html">Delete your account and data</a>.</li>
    <li><strong>Withdrawing consent</strong> &mdash; stop using the app and delete your account.</li>
    <li><strong>Revoking Google access</strong> &mdash; you can disconnect Trade Learn at
        <a href="https://myaccount.google.com/permissions">myaccount.google.com/permissions</a>.</li>
  </ul>

  <h2>10. Children</h2>
  <p>
    Trade Learn is not intended for children. You must be 18 or older to create an account. We do
    not knowingly collect data from anyone under 18; if we learn that we have, we delete it.
  </p>

  <h2>11. Security</h2>
  <p>
    Traffic is encrypted in transit. Sign-in uses Google and short-lived tokens rather than a
    password we store. Payment signatures are verified on our server before access is granted. No
    system is perfectly secure, but we take reasonable measures appropriate to the data involved.
  </p>

  <h2>12. Changes to this policy</h2>
  <p>
    If we change this policy we will update the date at the top of this page, and give notice in
    the app for anything significant.
  </p>

  <h2>13. Contact</h2>
  <p>
    <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a> &middot; WhatsApp {CONTACT_PHONE}
  </p>
""",
)

page(
    "account-deletion.html",
    "Delete your account and data",
    f"Last updated {UPDATED}",
    f"""
  <div class="box"><strong>You can do this yourself, in the app.</strong> Open
  <em>Account &rarr; Delete account</em> and confirm. It takes effect immediately and cannot be
  undone.</div>

  <h2>If you would rather ask us</h2>
  <p>Use either channel, from the contact details registered on your account:</p>
  <ul>
    <li><strong>Email</strong> &mdash; write to
      <a href="mailto:{CONTACT_EMAIL}?subject=Delete%20my%20Trade%20Learn%20account">{CONTACT_EMAIL}</a>
      from your registered email address, subject
      &ldquo;Delete my Trade Learn account&rdquo;.</li>
    <li><strong>WhatsApp</strong> &mdash; message <strong>{CONTACT_PHONE}</strong> from your
      registered mobile number.</li>
  </ul>

  <h2>What gets deleted</h2>
  <ul>
    <li>Your account: name, email address, mobile number, city and experience level.</li>
    <li>The Google account link, so signing in again creates a fresh account.</li>
    <li>Every practice trade you have opened or closed, and your practice portfolio.</li>
    <li>Your watchlist.</li>
    <li>All active sign-in sessions.</li>
  </ul>

  <h2>What is kept</h2>
  <p>
    Records of payments are retained for as long as tax and accounting law requires, even after the
    account is closed. They are not used for any other purpose.
  </p>

  <h2>What you lose</h2>
  <p>
    Any remaining paid days are forfeited &mdash; they are not refunded and cannot be moved to a new
    account.
  </p>

  <h2>How long it takes</h2>
  <p>
    Deleting from inside the app is immediate. A request by email or WhatsApp is verified and
    completed within <strong>7 days</strong>, and we confirm when it is done.
  </p>
""",
)

page(
    "support.html",
    "Support",
    "We usually reply within one working day",
    f"""
  <h2>Get in touch</h2>
  <ul>
    <li><strong>Email:</strong> <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></li>
    <li><strong>WhatsApp:</strong> {CONTACT_PHONE}</li>
  </ul>

  <h2>Common questions</h2>
  <p><strong>Is this real trading?</strong> No. Every position is simulated. Trade Learn never
     connects to your broker and never places an order. Nothing you do in the app can cost or make
     you real money.</p>
  <p><strong>Sign-in is not working.</strong> Trade Learn only supports Google sign-in. Make sure
     Google Play Services is up to date and that you picked the Google account you registered with.</p>
  <p><strong>Prices are not updating.</strong> Market data comes from a live feed that runs during
     NSE trading hours (9:15am&ndash;3:30pm IST, Monday to Friday). Outside those hours you will see
     the last close.</p>
  <p><strong>My trade closed on its own.</strong> That is the target, stop loss or trailing stop
     doing its job. The Live tab shows which one, and what the result was.</p>
  <p><strong>How do I delete my account?</strong> Account &rarr; Delete account, or see
     <a href="./account-deletion.html">Delete your account and data</a>.</p>
""",
)

page(
    "terms.html",
    "Terms of Service",
    f"Last updated {UPDATED}",
    f"""
  <div class="warn">
    <strong>Trade Learn is for practice and education only.</strong> Every trade is simulated. The
    app does not place real orders, does not connect to a broker, and does not handle securities.
    Nothing in it is investment advice or a recommendation to buy or sell anything.
  </div>

  <h2>1. Agreement</h2>
  <p>By creating an account or using Trade Learn, you agree to these terms. If you do not agree,
     please do not use the app.</p>

  <h2>2. What Trade Learn is</h2>
  <p>
    Trade Learn is a paper-trading practice tool. It shows live market data and generates trade
    ideas from it so you can practise reading a setup and managing a position. Positions exist only
    inside the app.
  </p>
  <p>
    We are not a stockbroker, an investment adviser, a research analyst, or a portfolio manager, and
    we are not registered with SEBI in any of those capacities.
  </p>

  <h2>3. Not investment advice</h2>
  <ul>
    <li>Signals, scores and targets are the output of automated analysis. They are educational
        material, not advice, and not a promise about what any market will do.</li>
    <li>Past performance of a strategy inside the app says nothing about future results.</li>
    <li>If you act on anything you learn here with real money, in a real broker account, you do so
        entirely at your own risk. Trading carries a substantial risk of loss.</li>
    <li>Consult a SEBI-registered adviser before making real investment decisions.</li>
  </ul>

  <h2>4. Your account</h2>
  <ul>
    <li>You must be 18 or older.</li>
    <li>Sign-in is through Google. Keep your Google account secure &mdash; anyone with it can reach
        your Trade Learn account.</li>
    <li>Give an accurate mobile number and keep it current. One number, one account.</li>
    <li>You are responsible for activity under your account.</li>
  </ul>

  <h2>5. Free trial and payment</h2>
  <ul>
    <li>New accounts include a free trial. After it ends, access is charged per day at the rate
        shown in the app before you pay.</li>
    <li>Days you buy are added to whatever access you already have &mdash; nothing is lost by paying
        early.</li>
    <li>Prices may change. The rate shown at the moment you pay is the rate you pay.</li>
    <li>Payments are processed by Razorpay. We never see your card or UPI details.</li>
    <li>Because access is delivered immediately and consumed by the day, purchased days are
        non-refundable except where the law requires otherwise, or where a technical fault on our
        side prevented you from using them &mdash; write to us and we will put it right.</li>
    <li>Deleting your account forfeits any remaining days.</li>
  </ul>

  <h2>6. Market data</h2>
  <p>
    Prices, candles and option chains come from third-party market data providers. We pass them
    through as received. They may be delayed, incomplete or wrong, and we do not warrant their
    accuracy. Do not rely on them for real trading decisions.
  </p>

  <h2>7. Acceptable use</h2>
  <p>Do not use the app to break the law, to attempt unauthorised access, to scrape or resell the
     market data or signals, or to disrupt the service for others.</p>

  <h2>8. Availability</h2>
  <p>We aim to keep the service running continuously but cannot guarantee uninterrupted
     availability. Maintenance, outages, market-data outages and factors outside our control can
     interrupt access.</p>

  <h2>9. Limitation of liability</h2>
  <p>
    To the maximum extent permitted by law we are not liable for indirect or consequential loss,
    lost profits, trading losses, or loss of data. Our total liability is limited to the amount you
    paid us in the twelve months before the claim.
  </p>

  <h2>10. Suspension and termination</h2>
  <p>We may suspend or close an account that breaches these terms. You may stop using the app and
     delete your account at any time from the Account screen.</p>

  <h2>11. Governing law</h2>
  <p>These terms are governed by the laws of India.</p>

  <h2>12. Contact</h2>
  <p><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
""",
)

print("done")
