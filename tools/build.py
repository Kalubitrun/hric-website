# -*- coding: utf-8 -*-
"""
Static site generator for the Haridwar Rai Inter College proposal site.

Everything here is written to plain HTML in the project root. Run with:

    python3 tools/build.py

All facts live in FACTS below, with a source note. Anything uncertain is
listed in PENDING.md — confirm before publishing.
"""

import os
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ----------------------------------------------------------------------------
# Verified facts (see PENDING.md for confidence + what still needs confirming)
# ----------------------------------------------------------------------------
SCHOOL_HI = "हरिद्वार राय इंटर कॉलेज"
SCHOOL_EN = "Haridwar Rai Inter College"
VILLAGE_HI = "भभनियाँव"
ADDRESS_HI = "ग्राम भभनियाँव, पोस्ट कमलपुर, ब्लॉक धानापुर, जिला चंदौली, उत्तर प्रदेश – 232106"
ADDRESS_SHORT_HI = "भभनियाँव, कमलपुर · जिला चंदौली (उ.प्र.) – 232106"
PHONE_DISPLAY = "+91 94515 70855"
PHONE_TEL = "+919451570855"
WA_NUMBER = "919451570855"
UDISE = "09660510204"
EST = "2000"
MAP_Q = "25.385612,83.37574"

WA_MSG = urllib.parse.quote(
    "नमस्ते, मुझे हरिद्वार राय इंटर कॉलेज में प्रवेश के बारे में जानकारी चाहिए।"
)
WA_LINK = "https://wa.me/%s?text=%s" % (WA_NUMBER, WA_MSG)

# ----------------------------------------------------------------------------
# Templates
# ----------------------------------------------------------------------------
HEAD = '''<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}}</title>
<meta name="description" content="{{DESC}}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#10263d">
<meta property="og:type" content="website">
<meta property="og:title" content="{{TITLE}}">
<meta property="og:description" content="{{DESC}}">
<meta property="og:locale" content="hi_IN">
<link rel="icon" href="{{ROOT}}assets/img/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;500;600;700&amp;family=Noto+Serif+Devanagari:wght@600;700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ROOT}}assets/css/style.css">
</head>
<body>

<div class="topbar">
  <div class="wrap">
    <span class="tb-left">उत्तर प्रदेश माध्यमिक शिक्षा परिषद (UP Board) से मान्यता प्राप्त</span>
    <span class="tb-right">
      <a href="tel:{{TEL}}">{{PHONE}}</a>
      <span class="sep">|</span>
      <a href="{{WA}}" target="_blank" rel="noopener">WhatsApp</a>
    </span>
  </div>
</div>

<header class="site-head">
  <div class="wrap">
    <a class="brand" href="{{ROOT}}index.html">
      <img src="{{ROOT}}assets/img/logo.svg" alt="विद्यालय चिह्न" width="44" height="44">
      <span>
        <b>हरिद्वार राय इंटर कॉलेज</b>
        <small>{{SHORT_ADDR}}</small>
      </span>
    </a>
    <nav class="nav" aria-label="मुख्य मेन्यू">
      {{NAV}}
    </nav>
  </div>
</header>

<div class="notice">
  <div class="wrap">
    <span class="notice-tag">सूचना</span>
    <p>प्रवेश एवं शुल्क संबंधी जानकारी के लिए विद्यालय कार्यालय से संपर्क करें — <a href="tel:{{TEL}}">{{PHONE}}</a></p>
  </div>
</div>

<main>
{{BODY}}
</main>

<footer class="site">
  <div class="wrap">
    <div class="cols">
      <div>
        <h4>हरिद्वार राय इंटर कॉलेज</h4>
        <p style="margin:0 0 10px">{{ADDRESS}}</p>
        <p style="margin:0 0 6px"><a href="tel:{{TEL}}">{{PHONE}}</a></p>
        <p style="margin:0"><a href="{{WA}}" target="_blank" rel="noopener">WhatsApp पर संपर्क करें</a></p>
      </div>
      <div>
        <h4>जानकारी</h4>
        <ul>
          <li><a href="{{ROOT}}about.html">विद्यालय परिचय</a></li>
          <li><a href="{{ROOT}}admission.html">प्रवेश</a></li>
          <li><a href="{{ROOT}}facilities.html">सुविधाएँ</a></li>
          <li><a href="{{ROOT}}contact.html">संपर्क</a></li>
        </ul>
      </div>
      <div>
        <h4>उपयोगी लिंक</h4>
        <ul>
          <li><a href="https://upmsp.edu.in/" target="_blank" rel="noopener">UP Board (UPMSP)</a></li>
          <li><a href="https://upresults.nic.in/" target="_blank" rel="noopener">बोर्ड परीक्षा परिणाम</a></li>
          <li><a href="{{ROOT}}en/index.html">English</a></li>
        </ul>
      </div>
    </div>
    <div class="bottom">
      <span>© <span id="yr">2026</span> हरिद्वार राय इंटर कॉलेज, {{VILLAGE}}</span>
      <span>UDISE कोड: {{UDISE}}</span>
    </div>
    <div class="proposal-note">
      यह वेबसाइट विद्यालय के लिए <b>प्रस्ताव</b> के रूप में तैयार की गई है। अंतिम प्रकाशन विद्यालय की स्वीकृति के पश्चात किया जाएगा।
    </div>
  </div>
</footer>

<script src="{{ROOT}}assets/js/main.js" defer></script>
</body>
</html>
'''

def _icon(inner):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
            + inner + '</svg>')


ICONS = {
    "physics": _icon('<circle cx="12" cy="12" r="2.2"/>'
                     '<ellipse cx="12" cy="12" rx="9.4" ry="4.1"/>'
                     '<ellipse cx="12" cy="12" rx="9.4" ry="4.1" transform="rotate(60 12 12)"/>'
                     '<ellipse cx="12" cy="12" rx="9.4" ry="4.1" transform="rotate(120 12 12)"/>'),
    "chem": _icon('<path d="M9 3h6"/>'
                  '<path d="M10 3v5.2L5.2 17a2.4 2.4 0 0 0 2.1 3.5h9.4a2.4 2.4 0 0 0 2.1-3.5L14 8.2V3"/>'
                  '<path d="M7.5 14h9"/>'),
    "book": _icon('<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/>'
                  '<path d="M4 20.5A2.5 2.5 0 0 1 6.5 18H20v3H6.5A2.5 2.5 0 0 1 4 20.5z"/>'),
    "water": _icon('<path d="M12 3.2s6 6.1 6 10.3a6 6 0 0 1-12 0C6 9.3 12 3.2 12 3.2z"/>'),
    "power": _icon('<path d="M13 2.5 4.5 13.5h6L10.5 21.5 19.5 10.5h-6z"/>'),
    "screen": _icon('<rect x="2.5" y="4" width="19" height="12.5" rx="1.5"/>'
                    '<path d="M9 20.5h6M12 16.5v4"/>'),
    "wash": _icon('<path d="M7 12.5V7a1.6 1.6 0 0 1 3.2 0v4.2"/>'
                  '<path d="M10.2 11V5.6a1.6 1.6 0 0 1 3.2 0v5.2"/>'
                  '<path d="M13.4 11V7.4a1.6 1.6 0 0 1 3.2 0v7.1a5.6 5.6 0 0 1-5.6 5.6h-.6a4 4 0 0 1-3.1-1.5L4 14.6"/>'),
    "wall": _icon('<rect x="2.5" y="5" width="19" height="14" rx="1"/>'
                  '<path d="M2.5 9.7h19M2.5 14.3h19M9 5v4.7M15 9.7v4.6M9 14.3V19"/>'),
    "printer": _icon('<path d="M6.5 9V3.5h11V9"/>'
                     '<rect x="2.5" y="9" width="19" height="7.5" rx="1.5"/>'
                     '<rect x="6.5" y="14" width="11" height="6.5" rx="1"/>'),
    "building": _icon('<path d="M3 9.5 12 4l9 5.5"/><path d="M5 10v9M9.5 10v9M14.5 10v9M19 10v9"/>'
                      '<path d="M3 19h18"/>'),
    "users": _icon('<circle cx="9" cy="8" r="3.2"/>'
                   '<path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5"/>'
                   '<path d="M16.5 5.2a3.2 3.2 0 0 1 0 6.1"/>'
                   '<path d="M18 14.8c2 .8 3.3 2.5 3.3 4.6"/>'),
    "records": _icon('<rect x="5" y="4" width="14" height="17" rx="1.5"/>'
                     '<path d="M9 4V2.8h6V4"/><path d="M8.5 10h7M8.5 14h7M8.5 18h4"/>'),
}

NAV_ITEMS = [
    ("index.html", "मुख्य पृष्ठ"),
    ("about.html", "परिचय"),
    ("admission.html", "प्रवेश"),
    ("facilities.html", "सुविधाएँ"),
    ("contact.html", "संपर्क"),
]


def nav(root, active):
    out = []
    for href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if href == active else ""
        out.append('<a href="%s%s"%s>%s</a>' % (root, href, cur, label))
    return "\n      ".join(out)


def render(title, desc, body, root="", active=""):
    html = (HEAD
            .replace("{{TITLE}}", title)
            .replace("{{DESC}}", desc)
            .replace("{{ROOT}}", root)
            .replace("{{NAV}}", nav(root, active))
            .replace("{{BODY}}", body)
            .replace("{{ADDRESS}}", ADDRESS_HI)
            .replace("{{SHORT_ADDR}}", ADDRESS_SHORT_HI)
            .replace("{{PHONE}}", PHONE_DISPLAY)
            .replace("{{TEL}}", PHONE_TEL)
            .replace("{{WA}}", WA_LINK)
            .replace("{{UDISE}}", UDISE)
            .replace("{{VILLAGE}}", VILLAGE_HI))
    for key, svg in ICONS.items():
        html = html.replace("{{I:%s}}" % key, svg)
    return html


def page_hero(title, sub, trail=""):
    crumb = '<p class="place">%s</p>' % trail if trail else ""
    return '''
<div class="hero" style="padding:48px 0 52px">
  <div class="wrap">
    %s
    <h1 style="font-size:clamp(26px,4vw,38px)">%s</h1>
    <p class="lead" style="margin-bottom:0">%s</p>
  </div>
</div>''' % (crumb, title, sub)


def band():
    return '''
<div class="band">
  <div class="wrap">
    <h2>प्रवेश संबंधी जानकारी चाहिए?</h2>
    <p>कार्यालय से सीधे बात करें, या WhatsApp पर संदेश भेजें — हम आपके सभी प्रश्नों का उत्तर देंगे।</p>
    <div class="btn-row">
      <a class="btn btn-wa" href="%s" target="_blank" rel="noopener">WhatsApp पर संदेश भेजें</a>
      <a class="btn btn-ghost" href="tel:%s">कॉल करें: %s</a>
    </div>
  </div>
</div>''' % (WA_LINK, PHONE_TEL, PHONE_DISPLAY)


GALLERY_CAPTIONS = [
    "विद्यालय भवन", "कक्षा-कक्ष", "विज्ञान प्रयोगशाला",
    "पुस्तकालय", "खेल गतिविधियाँ", "सांस्कृतिक कार्यक्रम",
]

PHOTO_ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="#5d6b7a" stroke-width="1.4" '
              'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
              '<rect x="3" y="5" width="18" height="14" rx="2"/>'
              '<circle cx="9" cy="10" r="1.6"/>'
              '<path d="M21 16l-5-5-5.5 5.5L8 14l-5 5"/></svg>')


def gallery():
    tiles = "\n".join(
        '      <div class="shot">%s<span>%s</span></div>' % (PHOTO_ICON, cap)
        for cap in GALLERY_CAPTIONS
    )
    return tiles


# ----------------------------------------------------------------------------
# Page bodies
# ----------------------------------------------------------------------------
HOME = '''
<div class="hero">
  <div class="wrap">
    <span class="pill">वर्ष 2000 से · UP Board से मान्यता प्राप्त</span>
    <h1>हरिद्वार राय इंटर कॉलेज</h1>
    <p class="place">%s</p>
    <p class="lead">कक्षा 6 से 12 तक हिंदी माध्यम में सह-शिक्षा। अनुशासन, संस्कार और बेहतर परिणाम के साथ विद्यार्थियों के भविष्य का मार्गदर्शन।</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="admission.html">प्रवेश जानकारी</a>
      <a class="btn btn-wa" href="%s" target="_blank" rel="noopener">WhatsApp पर बात करें</a>
      <a class="btn btn-ghost" href="tel:%s">कॉल करें</a>
    </div>
  </div>
</div>

<div class="stats">
  <div class="wrap">
    <div class="stat"><b>2000</b><span>स्थापना वर्ष</span></div>
    <div class="stat"><b>6–12</b><span>कक्षाएँ</span></div>
    <div class="stat"><b>1,700+</b><span>विद्यार्थी</span></div>
    <div class="stat"><b>25+</b><span>वर्षों की सेवा</span></div>
  </div>
</div>

<section class="block">
  <div class="wrap">
    <span class="eyebrow">विद्यालय परिचय</span>
    <h2 class="title">गाँव और कस्बे के विद्यार्थियों के लिए एक भरोसेमंद शिक्षण संस्थान</h2>
    <p class="sub">वर्ष 2000 में स्थापित यह विद्यालय उत्तर प्रदेश माध्यमिक शिक्षा परिषद (UP Board) से मान्यता प्राप्त है और कक्षा 6 से 12 तक हिंदी माध्यम में शिक्षा प्रदान करता है।</p>

    <div class="grid c2" style="align-items:start">
      <div>
        <p>विद्यालय का उद्देश्य है कि आस-पास के गाँवों के विद्यार्थियों को शहर जाकर पढ़ने की मजबूरी न हो। यहाँ विद्यार्थियों को बोर्ड परीक्षा की तैयारी के साथ-साथ अनुशासन, संस्कार और आत्मविश्वास भी सिखाया जाता है।</p>
        <p>विद्यालय में विज्ञान प्रयोगशालाएँ, पुस्तकालय एवं पुस्तक बैंक तथा पढ़ाई के लिए आवश्यक अन्य सुविधाएँ उपलब्ध हैं। अनुभवी शिक्षक विद्यार्थियों की व्यक्तिगत रूप से सहायता करते हैं।</p>
        <p style="margin-bottom:0"><a class="btn btn-dark" href="about.html">पूरा परिचय पढ़ें</a></p>
      </div>
      <table class="facts">
        <tr><th>स्थापना वर्ष</th><td>2000</td></tr>
        <tr><th>बोर्ड</th><td>उत्तर प्रदेश माध्यमिक शिक्षा परिषद (UP Board)</td></tr>
        <tr><th>कक्षाएँ</th><td>कक्षा 6 से 12</td></tr>
        <tr><th>माध्यम</th><td>हिंदी</td></tr>
        <tr><th>प्रकार</th><td>सह-शिक्षा (बालक एवं बालिका)</td></tr>
        <tr><th>प्रबंधन</th><td>निजी संस्था (मान्यता प्राप्त)</td></tr>
        <tr><th>UDISE कोड</th><td>%s</td></tr>
      </table>
    </div>
  </div>
</section>

<section class="block alt">
  <div class="wrap">
    <span class="eyebrow">सुविधाएँ</span>
    <h2 class="title">पढ़ाई के लिए ज़रूरी सुविधाएँ</h2>
    <p class="sub">विद्यालय में उपलब्ध मुख्य सुविधाओं की जानकारी।</p>
    <div class="grid c3">
      <div class="card"><div class="ico">{{I:physics}}</div><h3>भौतिक विज्ञान प्रयोगशाला</h3><p>विद्यार्थियों के व्यावहारिक अभ्यास के लिए सुसज्जित प्रयोगशाला।</p></div>
      <div class="card"><div class="ico">{{I:chem}}</div><h3>रसायन विज्ञान प्रयोगशाला</h3><p>प्रयोग एवं परीक्षा की तैयारी हेतु आवश्यक उपकरण एवं सामग्री।</p></div>
      <div class="card"><div class="ico">{{I:book}}</div><h3>पुस्तकालय एवं पुस्तक बैंक</h3><p>पाठ्यपुस्तकों के अतिरिक्त संदर्भ पुस्तकें एवं पुस्तक बैंक की सुविधा।</p></div>
      <div class="card"><div class="ico">{{I:water}}</div><h3>पेयजल एवं स्वच्छता</h3><p>शुद्ध पेयजल तथा हैंडवॉश की व्यवस्था।</p></div>
      <div class="card"><div class="ico">{{I:power}}</div><h3>विद्युत बैकअप</h3><p>बिजली जाने पर भी पढ़ाई बाधित न हो, इसके लिए जनरेटर की सुविधा।</p></div>
      <div class="card"><div class="ico">{{I:screen}}</div><h3>डिजिटल बोर्ड</h3><p>कक्षा-कक्षों में डिजिटल बोर्ड के माध्यम से पठन-पाठन।</p></div>
    </div>
    <p style="margin-top:26px"><a class="btn btn-dark" href="facilities.html">सभी सुविधाएँ देखें</a></p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <span class="eyebrow">प्रवेश</span>
    <h2 class="title">प्रवेश प्रक्रिया — तीन आसान चरण</h2>
    <p class="sub">प्रवेश कक्षा 6, 9 एवं 11 में लिए जाते हैं। सीटें सीमित हैं, अतः समय पर संपर्क करें।</p>
    <div class="steps">
      <div class="step"><h3>कार्यालय से संपर्क</h3><p>विद्यालय कार्यालय में जाकर या फ़ोन/WhatsApp द्वारा प्रवेश फ़ॉर्म के बारे में जानकारी लें।</p></div>
      <div class="step"><h3>दस्तावेज़ जमा करें</h3><p>आवश्यक दस्तावेज़ों के साथ फ़ॉर्म कार्यालय में जमा करें।</p></div>
      <div class="step"><h3>प्रवेश की पुष्टि</h3><p>दस्तावेज़ जाँच के बाद विद्यार्थी का नाम प्रवेश सूची में जोड़ा जाता है तथा शुल्क जमा किया जाता है।</p></div>
    </div>
  </div>
</section>

<section class="block alt">
  <div class="wrap">
    <span class="eyebrow">गैलरी</span>
    <h2 class="title">विद्यालय की झलक</h2>
    <p class="sub">विद्यालय परिसर, कक्षाओं एवं गतिविधियों की कुछ तस्वीरें।</p>
    <div class="gallery">
%s
    </div>
  </div>
</section>

%s
''' % (ADDRESS_SHORT_HI, WA_LINK, PHONE_TEL, UDISE, gallery(), band())


ABOUT = '''
<div class="hero" style="padding:48px 0 52px">
  <div class="wrap">
    <p class="place">मुख्य पृष्ठ / परिचय</p>
    <h1 style="font-size:clamp(26px,4vw,38px)">विद्यालय परिचय</h1>
    <p class="lead" style="margin-bottom:0">स्थापना 2000 · UP Board से मान्यता प्राप्त · कक्षा 6 से 12</p>
  </div>
</div>

<section class="block">
  <div class="wrap">
    <div class="grid c2" style="align-items:start">
      <div>
        <span class="eyebrow">हमारे बारे में</span>
        <h2 class="title">गाँव के विद्यार्थियों के लिए बेहतर शिक्षा</h2>
        <p>हरिद्वार राय इंटर कॉलेज की स्थापना वर्ष 2000 में हुई। विद्यालय उत्तर प्रदेश माध्यमिक शिक्षा परिषद (UP Board) से मान्यता प्राप्त है तथा कक्षा 6 से 12 तक हिंदी माध्यम में सह-शिक्षा प्रदान करता है।</p>
        <p>विद्यालय का संचालन एक निजी शिक्षण संस्था द्वारा किया जाता है। यहाँ का उद्देश्य आस-पास के ग्रामीण क्षेत्रों के विद्यार्थियों को अपने ही क्षेत्र में गुणवत्तापूर्ण माध्यमिक शिक्षा उपलब्ध कराना है, जिससे उन्हें पढ़ाई के लिए दूर जाना न पड़े।</p>
        <p>विद्यालय में विज्ञान प्रयोगशालाएँ, पुस्तकालय एवं पुस्तक बैंक, पेयजल एवं स्वच्छता की सुविधा तथा कक्षा-कक्षों में डिजिटल बोर्ड उपलब्ध हैं।</p>
      </div>
      <table class="facts">
        <tr><th>विद्यालय का नाम</th><td>हरिद्वार राय इंटर कॉलेज</td></tr>
        <tr><th>स्थापना वर्ष</th><td>2000</td></tr>
        <tr><th>बोर्ड</th><td>उत्तर प्रदेश माध्यमिक शिक्षा परिषद</td></tr>
        <tr><th>कक्षाएँ</th><td>6 से 12</td></tr>
        <tr><th>माध्यम</th><td>हिंदी</td></tr>
        <tr><th>प्रकार</th><td>सह-शिक्षा</td></tr>
        <tr><th>प्रबंधन</th><td>निजी संस्था (मान्यता प्राप्त)</td></tr>
        <tr><th>स्थान</th><td>ग्रामीण क्षेत्र, ब्लॉक धानापुर</td></tr>
        <tr><th>UDISE कोड</th><td>%s</td></tr>
        <tr><th>पिन कोड</th><td>232106</td></tr>
      </table>
    </div>
  </div>
</section>

<section class="block alt">
  <div class="wrap">
    <span class="eyebrow">मान्यता एवं प्रबंधन</span>
    <h2 class="title">विद्यालय की औपचारिक जानकारी</h2>
    <p class="sub">नीचे दी गई जानकारी विद्यालय के सरकारी अभिलेखों पर आधारित है।</p>
    <div class="grid c3">
      <div class="card"><div class="ico">{{I:building}}</div><h3>मान्यता</h3><p>उत्तर प्रदेश माध्यमिक शिक्षा परिषद (UP Board) से मान्यता प्राप्त, वर्ष 2000 से।</p></div>
      <div class="card"><div class="ico">{{I:users}}</div><h3>प्रबंधन</h3><p>विद्यालय का संचालन एक निजी शिक्षण संस्था द्वारा किया जाता है।</p></div>
      <div class="card"><div class="ico">{{I:records}}</div><h3>अभिलेख</h3><p>UDISE कोड: %s · श्रेणी: उच्च प्राथमिक से माध्यमिक एवं इंटरमीडिएट</p></div>
    </div>
    <div class="note" style="margin-top:26px">
      <b>प्रधानाचार्य:</b> डॉ. रामप्रताप राय — विद्यालय कार्यालय में उपलब्ध समय पर मिल सकते हैं।
    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <span class="eyebrow">संदेश</span>
    <h2 class="title">प्रधानाचार्य का संदेश</h2>
    <div class="card" style="max-width:820px">
      <p style="font-size:17px;color:#1c2430">प्रिय विद्यार्थी एवं अभिभावक,</p>
      <p style="font-size:17px;color:#1c2430">शिक्षा वह माध्यम है जो व्यक्ति के जीवन की दिशा बदल देता है। हमारा प्रयास है कि यहाँ पढ़ने वाला प्रत्येक विद्यार्थी न केवल परीक्षा में सफल हो, बल्कि एक अनुशासित और आत्मविश्वासी नागरिक बने।</p>
      <p style="font-size:17px;color:#1c2430;margin-bottom:0">हमारे शिक्षक विद्यार्थियों की समस्याओं को ध्यान से सुनते हैं और उन्हें सही दिशा देने का प्रयास करते हैं। आपके सहयोग से हम इस विद्यालय को और बेहतर बना सकते हैं।</p>
    </div>
  </div>
</section>

%s
''' % (UDISE, UDISE, band())


ADMISSION = '''
<div class="hero" style="padding:48px 0 52px">
  <div class="wrap">
    <p class="place">मुख्य पृष्ठ / प्रवेश</p>
    <h1 style="font-size:clamp(26px,4vw,38px)">प्रवेश</h1>
    <p class="lead" style="margin-bottom:0">कक्षा 6, 9 एवं 11 में प्रवेश</p>
  </div>
</div>

<section class="block">
  <div class="wrap">
    <span class="eyebrow">प्रवेश कक्षाएँ</span>
    <h2 class="title">किन कक्षाओं में प्रवेश होता है</h2>
    <p class="sub">विद्यालय में मुख्य रूप से निम्नलिखित कक्षाओं में प्रवेश लिया जाता है।</p>
    <div class="grid c3">
      <div class="card"><div class="ico">6</div><h3>कक्षा 6</h3><p>उच्च प्राथमिक स्तर का प्रारंभ। नए विद्यार्थियों के लिए प्रवेश।</p></div>
      <div class="card"><div class="ico">9</div><h3>कक्षा 9</h3><p>हाईस्कूल का प्रारंभ। इस स्तर पर सबसे अधिक प्रवेश होते हैं।</p></div>
      <div class="card"><div class="ico">11</div><h3>कक्षा 11</h3><p>इंटरमीडिएट का प्रारंभ। विषय/संकाय का चयन इसी समय होता है।</p></div>
    </div>
    <div class="note" style="margin-top:26px">
      <b>ध्यान दें:</b> कक्षा 11 में प्रवेश हेतु विषयों की उपलब्धता एवं न्यूनतम योग्यता की जानकारी कार्यालय से अवश्य प्राप्त करें।
    </div>
  </div>
</section>

<section class="block alt">
  <div class="wrap">
    <span class="eyebrow">प्रक्रिया</span>
    <h2 class="title">प्रवेश की प्रक्रिया</h2>
    <div class="steps">
      <div class="step"><h3>जानकारी लें</h3><p>कार्यालय जाकर, फ़ोन करके या WhatsApp पर संदेश भेजकर प्रवेश फ़ॉर्म एवं तिथियों की जानकारी प्राप्त करें।</p></div>
      <div class="step"><h3>फ़ॉर्म एवं दस्तावेज़</h3><p>प्रवेश फ़ॉर्म भरकर आवश्यक दस्तावेज़ों की छायाप्रति के साथ कार्यालय में जमा करें।</p></div>
      <div class="step"><h3>सत्यापन एवं शुल्क</h3><p>दस्तावेज़ों की जाँच के बाद प्रवेश की पुष्टि की जाती है तथा शुल्क जमा किया जाता है।</p></div>
    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <div class="grid c2" style="align-items:start">
      <div>
        <span class="eyebrow">दस्तावेज़</span>
        <h2 class="title">आवश्यक दस्तावेज़</h2>
        <ul style="padding-left:20px;margin:0;color:#1c2430">
          <li>आधार कार्ड की छायाप्रति</li>
          <li>पिछली कक्षा की अंकतालिका / मार्कशीट</li>
          <li>स्थानांतरण प्रमाण पत्र (TC)</li>
          <li>जन्म प्रमाण पत्र</li>
          <li>निवास प्रमाण पत्र</li>
          <li>जाति प्रमाण पत्र (यदि लागू हो)</li>
          <li>विद्यार्थी एवं अभिभावक के दो-दो पासपोर्ट आकार के फ़ोटो</li>
        </ul>
        <p style="margin-top:18px;color:#5d6b7a;font-size:15.5px">दस्तावेज़ों की मूल प्रतियाँ सत्यापन के समय साथ लाएँ।</p>
      </div>
      <div>
        <span class="eyebrow">शुल्क</span>
        <h2 class="title">शुल्क संबंधी जानकारी</h2>
        <table class="facts">
          <tr><th>कक्षा 6 – 8</th><td>कार्यालय से जानकारी लें</td></tr>
          <tr><th>कक्षा 9 – 10</th><td>कार्यालय से जानकारी लें</td></tr>
          <tr><th>कक्षा 11 – 12</th><td>कार्यालय से जानकारी लें</td></tr>
        </table>
        <div class="note" style="margin-top:18px">
          शुल्क की वर्तमान दरें, परीक्षा शुल्क एवं अन्य शुल्कों की जानकारी विद्यालय कार्यालय से प्राप्त करें।
        </div>
        <p style="margin-top:18px"><a class="btn btn-wa" href="%s" target="_blank" rel="noopener">WhatsApp पर शुल्क पूछें</a></p>
      </div>
    </div>
  </div>
</section>

%s
''' % (WA_LINK, band())


FACILITIES = '''
<div class="hero" style="padding:48px 0 52px">
  <div class="wrap">
    <p class="place">मुख्य पृष्ठ / सुविधाएँ</p>
    <h1 style="font-size:clamp(26px,4vw,38px)">सुविधाएँ</h1>
    <p class="lead" style="margin-bottom:0">विद्यार्थियों की पढ़ाई और सुरक्षा के लिए उपलब्ध व्यवस्थाएँ</p>
  </div>
</div>

<section class="block">
  <div class="wrap">
    <span class="eyebrow">परिसर</span>
    <h2 class="title">विद्यालय में उपलब्ध सुविधाएँ</h2>
    <p class="sub">नीचे दी गई सुविधाओं की जानकारी विद्यालय के अभिलेखों के अनुसार है।</p>
    <div class="grid c3">
      <div class="card"><div class="ico">{{I:physics}}</div><h3>भौतिक विज्ञान प्रयोगशाला</h3><p>विद्यार्थी प्रयोग करके सीखें, इसके लिए आवश्यक उपकरणों सहित प्रयोगशाला।</p></div>
      <div class="card"><div class="ico">{{I:chem}}</div><h3>रसायन विज्ञान प्रयोगशाला</h3><p>रसायन विज्ञान के प्रयोगों एवं व्यावहारिक परीक्षा की तैयारी हेतु।</p></div>
      <div class="card"><div class="ico">{{I:book}}</div><h3>पुस्तकालय एवं पुस्तक बैंक</h3><p>पाठ्यपुस्तकों के अतिरिक्त संदर्भ पुस्तकें; ज़रूरतमंद विद्यार्थियों के लिए पुस्तक बैंक।</p></div>
      <div class="card"><div class="ico">{{I:water}}</div><h3>पेयजल</h3><p>विद्यार्थियों के लिए शुद्ध पेयजल की व्यवस्था।</p></div>
      <div class="card"><div class="ico">{{I:wash}}</div><h3>हैंडवॉश एवं स्वच्छता</h3><p>हाथ धोने की सुविधा तथा स्वच्छता पर विशेष ध्यान।</p></div>
      <div class="card"><div class="ico">{{I:power}}</div><h3>विद्युत बैकअप</h3><p>बिजली बाधित होने पर भी कक्षाएँ चलती रहें, इसके लिए जनरेटर।</p></div>
      <div class="card"><div class="ico">{{I:screen}}</div><h3>डिजिटल बोर्ड</h3><p>कक्षा-कक्षों में डिजिटल बोर्ड द्वारा पठन-पाठन।</p></div>
      <div class="card"><div class="ico">{{I:wall}}</div><h3>पक्की चारदीवारी</h3><p>विद्यालय परिसर पक्की चारदीवारी से घिरा हुआ है।</p></div>
      <div class="card"><div class="ico">{{I:printer}}</div><h3>कार्यालय सुविधा</h3><p>प्रिंटर, स्कैनर एवं कंप्यूटर — अभिलेखों एवं प्रमाण पत्रों के लिए।</p></div>
    </div>
  </div>
</section>

<section class="block alt">
  <div class="wrap">
    <span class="eyebrow">कक्षाएँ</span>
    <h2 class="title">पठन-पाठन की व्यवस्था</h2>
    <div class="grid c2" style="align-items:start">
      <div class="card">
        <h3 style="margin-top:0">हिंदी माध्यम, सह-शिक्षा</h3>
        <p>विद्यालय में बालक एवं बालिकाएँ साथ पढ़ते हैं। पठन-पाठन का माध्यम हिंदी है तथा पाठ्यक्रम UP Board के अनुसार है।</p>
      </div>
      <div class="card">
        <h3 style="margin-top:0">कक्षा 6 से 12</h3>
        <p>उच्च प्राथमिक (6–8), माध्यमिक (9–10) एवं इंटरमीडिएट (11–12) — तीनों स्तरों की कक्षाएँ संचालित हैं।</p>
      </div>
    </div>
    <div class="note" style="margin-top:22px">
      किसी विशेष सुविधा, विषय या संकाय के बारे में जानकारी के लिए विद्यालय कार्यालय से संपर्क करें।
    </div>
  </div>
</section>

%s
''' % band()


CONTACT = '''
<div class="hero" style="padding:48px 0 52px">
  <div class="wrap">
    <p class="place">मुख्य पृष्ठ / संपर्क</p>
    <h1 style="font-size:clamp(26px,4vw,38px)">संपर्क करें</h1>
    <p class="lead" style="margin-bottom:0">प्रवेश, शुल्क या किसी भी जानकारी के लिए हमसे संपर्क करें।</p>
  </div>
</div>

<section class="block">
  <div class="wrap">
    <div class="contact-grid">
      <div>
        <span class="eyebrow">पता एवं संपर्क</span>
        <h2 class="title">विद्यालय कार्यालय</h2>
        <ul class="info-list">
          <li>
            <div>
              <div class="k">पता</div>
              <div class="v">%s</div>
            </div>
          </li>
          <li>
            <div>
              <div class="k">फ़ोन</div>
              <div class="v"><a href="tel:%s">%s</a></div>
            </div>
          </li>
          <li>
            <div>
              <div class="k">WhatsApp</div>
              <div class="v"><a href="%s" target="_blank" rel="noopener">संदेश भेजें</a></div>
            </div>
          </li>
          <li>
            <div>
              <div class="k">कार्यालय समय</div>
              <div class="v">सोमवार – शनिवार (अवकाश के दिनों को छोड़कर)</div>
            </div>
          </li>
          <li>
            <div>
              <div class="k">UDISE कोड</div>
              <div class="v">%s</div>
            </div>
          </li>
        </ul>
        <div class="map-frame" style="margin-top:20px">
          <iframe src="https://maps.google.com/maps?q=%s&amp;hl=hi&amp;z=15&amp;output=embed"
                  title="विद्यालय का नक्शा" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        <p style="margin:10px 0 0;font-size:14.5px"><a href="https://www.google.com/maps/search/?api=1&amp;query=25.385612,83.37574" target="_blank" rel="noopener">Google Maps पर खोलें →</a></p>
      </div>

      <div>
        <span class="eyebrow">संदेश</span>
        <h2 class="title">अपनी जानकारी भेजें</h2>
        <p class="sub" style="margin-bottom:16px">नीचे जानकारी भरें — “WhatsApp पर भेजें” दबाने पर संदेश सीधे विद्यालय के WhatsApp पर खुल जाएगा।</p>
        <form class="enquiry" id="enquiry-form">
          <div>
            <label for="f-name">आपका नाम</label>
            <input id="f-name" name="name" type="text" placeholder="पूरा नाम" required>
          </div>
          <div>
            <label for="f-phone">मोबाइल नंबर</label>
            <input id="f-phone" name="phone" type="tel" inputmode="numeric" placeholder="10 अंकों का नंबर" required>
          </div>
          <div>
            <label for="f-class">कक्षा</label>
            <select id="f-class" name="class">
              <option>कक्षा 6</option>
              <option>कक्षा 7</option>
              <option>कक्षा 8</option>
              <option>कक्षा 9</option>
              <option>कक्षा 10</option>
              <option>कक्षा 11</option>
              <option>कक्षा 12</option>
            </select>
          </div>
          <div>
            <label for="f-msg">संदेश (वैकल्पिक)</label>
            <textarea id="f-msg" name="message" placeholder="आप क्या जानना चाहते हैं?"></textarea>
          </div>
          <button class="btn btn-wa" type="submit" style="justify-content:center">WhatsApp पर भेजें</button>
          <p class="hint">कोई शुल्क नहीं। आपकी जानकारी केवल विद्यालय कार्यालय तक पहुँचेगी।</p>
        </form>
      </div>
    </div>
  </div>
</section>

%s
''' % (ADDRESS_HI, PHONE_TEL, PHONE_DISPLAY, WA_LINK, UDISE, MAP_Q, band())


EN_PAGE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Haridwar Rai Inter College — Bhabhaniyav, Kamalpur, Chandauli</title>
<meta name="description" content="Haridwar Rai Inter College, Bhabhaniyav (Kamalpur), Block Dhanapur, District Chandauli, Uttar Pradesh — affiliated to UP Board, classes 6 to 12, Hindi medium.">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#10263d">
<link rel="icon" href="../assets/img/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="../assets/css/style.css">
</head>
<body class="lang-en">

<div class="topbar">
  <div class="wrap">
    <span class="tb-left">Affiliated to the Uttar Pradesh Board of High School &amp; Intermediate Education</span>
    <span class="tb-right">
      <a href="tel:+919451570855">+91 94515 70855</a>
      <span class="sep">|</span>
      <a href="https://wa.me/919451570855" target="_blank" rel="noopener">WhatsApp</a>
    </span>
  </div>
</div>

<header class="site-head">
  <div class="wrap">
    <a class="brand" href="index.html">
      <img src="../assets/img/logo.svg" alt="School emblem" width="46" height="46">
      <span>
        <b>Haridwar Rai Inter College</b>
        <small>Bhabhaniyav, Kamalpur · Chandauli (U.P.) – 232106</small>
      </span>
    </a>
    <nav class="nav" aria-label="Main menu">
      <a href="../index.html">हिंदी</a>
      <a href="index.html" aria-current="page">English</a>
    </nav>
  </div>
</header>

<main>
<div class="hero">
  <div class="wrap">
    <span class="pill">Established 2000 · UP Board affiliated</span>
    <h1>Haridwar Rai Inter College</h1>
    <p class="place">Bhabhaniyav, Post Kamalpur, Block Dhanapur, District Chandauli, Uttar Pradesh – 232106</p>
    <p class="lead">Classes 6 to 12 · Hindi medium · Co-educational. Serving students of the Dhanapur block since 2000.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="#contact">Admission enquiry</a>
      <a class="btn btn-wa" href="https://wa.me/919451570855" target="_blank" rel="noopener">WhatsApp</a>
    </div>
  </div>
</div>

<section class="block">
  <div class="wrap">
    <span class="eyebrow">About the school</span>
    <h2 class="title">A neighbourhood institution for rural students</h2>
    <p class="sub">Haridwar Rai Inter College was established in 2000 and is recognised by the Uttar Pradesh Board of High School and Intermediate Education (UP Board). It is a privately managed, co-educational institution offering Hindi-medium education from class 6 to class 12.</p>
    <div class="grid c2" style="align-items:start">
      <div>
        <p>The college exists so that students from the surrounding villages can complete their schooling close to home instead of travelling to the city.</p>
        <p>Facilities include physics and chemistry laboratories, a library and book bank, clean drinking water and handwashing facilities, a generator for power backup, and digital boards in classrooms.</p>
      </div>
      <table class="facts">
        <tr><th>Established</th><td>2000</td></tr>
        <tr><th>Board</th><td>Uttar Pradesh Board (UP Board)</td></tr>
        <tr><th>Classes</th><td>6 to 12</td></tr>
        <tr><th>Medium</th><td>Hindi</td></tr>
        <tr><th>Type</th><td>Co-educational</td></tr>
        <tr><th>Management</th><td>Private (recognised)</td></tr>
        <tr><th>UDISE code</th><td>09660510204</td></tr>
      </table>
    </div>
  </div>
</section>

<section class="block alt" id="contact">
  <div class="wrap">
    <span class="eyebrow">Contact</span>
    <h2 class="title">Get in touch</h2>
    <p class="sub">For admission, fees or any other information, please contact the school office.</p>
    <div class="grid c2" style="align-items:start">
      <ul class="info-list">
        <li><div><div class="k">Address</div><div class="v">Bhabhaniyav, Post Kamalpur, Block Dhanapur, District Chandauli, Uttar Pradesh – 232106</div></div></li>
        <li><div><div class="k">Phone</div><div class="v"><a href="tel:+919451570855">+91 94515 70855</a></div></div></li>
        <li><div><div class="k">Office hours</div><div class="v">Monday to Saturday (except holidays)</div></div></li>
      </ul>
      <div>
        <div class="map-frame">
        <iframe src="https://maps.google.com/maps?q=25.385612,83.37574&amp;hl=en&amp;z=15&amp;output=embed"
                title="School location" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        <p style="margin:10px 0 0;font-size:14.5px"><a href="https://www.google.com/maps/search/?api=1&amp;query=25.385612,83.37574" target="_blank" rel="noopener">Open in Google Maps &rarr;</a></p>
      </div>
    </div>
  </div>
</section>
</main>

<footer class="site">
  <div class="wrap">
    <div class="bottom" style="margin-top:0;border-top:0;padding-top:0">
      <span>© 2026 Haridwar Rai Inter College, Bhabhaniyav</span>
      <span>UDISE code: 09660510204</span>
    </div>
    <div class="proposal-note">
      This site has been prepared as a <b>proposal</b> for the school. It will be published only after the school's approval.
    </div>
  </div>
</footer>

</body>
</html>
'''


# ----------------------------------------------------------------------------
# Write everything
# ----------------------------------------------------------------------------
PAGES = [
    ("index.html", "हरिद्वार राय इंटर कॉलेज | भभनियाँव, कमलपुर — चंदौली",
     "हरिद्वार राय इंटर कॉलेज, भभनियाँव (कमलपुर), ब्लॉक धानापुर, जिला चंदौली — UP Board से मान्यता प्राप्त, कक्षा 6 से 12, हिंदी माध्यम। प्रवेश, सुविधाएँ एवं संपर्क जानकारी।",
     HOME, "index.html"),

    ("about.html", "विद्यालय परिचय | हरिद्वार राय इंटर कॉलेज",
     "हरिद्वार राय इंटर कॉलेज का परिचय — स्थापना 2000, UP Board से मान्यता, कक्षा 6 से 12, हिंदी माध्यम, निजी प्रबंधन एवं UDISE विवरण।",
     ABOUT, "about.html"),

    ("admission.html", "प्रवेश | हरिद्वार राय इंटर कॉलेज",
     "कक्षा 6, 9 एवं 11 में प्रवेश — प्रक्रिया, आवश्यक दस्तावेज़ एवं शुल्क संबंधी जानकारी। हरिद्वार राय इंटर कॉलेज, भभनियाँव, चंदौली।",
     ADMISSION, "admission.html"),

    ("facilities.html", "सुविधाएँ | हरिद्वार राय इंटर कॉलेज",
     "विद्यालय में उपलब्ध सुविधाएँ — विज्ञान प्रयोगशालाएँ, पुस्तकालय एवं पुस्तक बैंक, पेयजल, विद्युत बैकअप एवं डिजिटल बोर्ड।",
     FACILITIES, "facilities.html"),

    ("contact.html", "संपर्क | हरिद्वार राय इंटर कॉलेज",
     "हरिद्वार राय इंटर कॉलेज से संपर्क करें — पता, फ़ोन नंबर, WhatsApp, नक्शा एवं कार्यालय समय।",
     CONTACT, "contact.html"),
]


def main():
    for filename, title, desc, body, active in PAGES:
        html = render(title, desc, body, root="", active=active)
        path = os.path.join(ROOT, filename)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
        print("wrote", filename, len(html), "bytes")

    with open(os.path.join(ROOT, "en", "index.html"), "w", encoding="utf-8") as fh:
        fh.write(EN_PAGE)
    print("wrote en/index.html", len(EN_PAGE), "bytes")

    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write("# Proposal build — not for indexing until approved.\nUser-agent: *\nDisallow: /\n")
    print("wrote robots.txt")


if __name__ == "__main__":
    main()
