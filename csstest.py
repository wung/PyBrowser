import cssutils

sheet = cssutils.parseString("""
/* Trac CSS */
body {
 background: #fff;
 color: #000;
 margin: 10px;
}
body, th, td {
 font: normal 13px verdana,arial,'Bitstream Vera Sans',helvetica,sans-serif;
}
h1, h2, h3, h4 {
 font-family: arial,verdana,'Bitstream Vera Sans',helvetica,sans-serif;
 font-weight: bold;
 letter-spacing: -0.018em;
}
h1 { font-size: 21px; margin: .15em 1em 0 0 }
h2 { font-size: 16px; margin: 2em 0 .5em; }
h3 { font-size: 14px; margin: 1.5em 0 .5em; }
hr { border: none;  border-top: 1px solid #ccb; margin: 2em 0; }
address { font-style: normal }
img { border: none }

.underline { text-decoration: underline; }
ol.loweralpha { list-style-type: lower-alpha }
ol.upperalpha { list-style-type: upper-alpha }
ol.lowerroman { list-style-type: lower-roman }
ol.upperroman { list-style-type: upper-roman }
ol.arabic     { list-style-type: decimal }

/* Link styles */
:link, :visited {
 text-decoration: none;
 color: #b00;
 border-bottom: 1px dotted #bbb;
}
:link:hover, :visited:hover {
 background-color: #eee;
 color: #555;
}
h1 :link, h1 :visited ,h2 :link, h2 :visited, h3 :link, h3 :visited,
h4 :link, h4 :visited, h5 :link, h5 :visited, h6 :link, h6 :visited {
 color: inherit;
}

.ext-link { background: url(../extlink.gif) no-repeat 0 58%; padding-left: 16px }
* html .ext-link { background-position: 0 .35em } /* IE hack, see #937 */

/* Forms */
input, textarea, select { margin: 2px }
input, select { vertical-align: middle }
input[type=submit], input[type=reset] {
 background: #eee;
 color: #222;
 border: 1px outset #ccc;
 padding: .1em .5em;
}
input[type=submit]:hover, input[type=reset]:hover { background: #ccb }
input[type=text], input.textwidget, textarea {
 background: #fff;
 color: #000;
 border: 1px solid #d7d7d7;
}
input[type=text], input.textwidget { padding: .25em .5em }
input[type=text]:focus, textarea:focus { border: 1px solid #886 }
option { border-bottom: 1px dotted #d7d7d7 }
fieldset { border: 1px solid #d7d7d7; padding: .5em; margin: 0 }
fieldset.iefix { border: none; padding: 0; margin: 0 }
* html fieldset.iefix { width: 98% }
fieldset.iefix p { margin: 0 }
legend { color: #999; padding: 0 .25em; font-size: 90%; font-weight: bold }
label.disabled { color: #d7d7d7 }
.buttons { margin: .5em .5em .5em 0 }
.buttons form, .buttons form div { display: inline }
.buttons input { margin: 1em .5em .1em 0 }

/* Header */
#header hr { display: none }
#header img { border: none; margin: 0 0 -3em }
#header :link, #header :visited, #header :link:hover, #header :visited:hover {
 background: transparent;
 margin-bottom: 2px;
 border: none;
}

/* Quick search */
#search {
 clear: both;
 font-size: 10px;
 height: 2.2em;
 margin: 0 0 1em;
 text-align: right;
}
#search input { font-size: 10px }
#search label { display: none }

/* Navigation */
.nav { height: 1em }
.nav h2, .nav hr { display: none }
.nav ul {
 display: block;
 font-size: 10px;
 margin: 0;
 padding: 0 0 .25em;
 text-align: right;
}
.nav li {
 display: inline;
 border-right: 1px solid #d7d7d7;
 list-style: none;
 padding: 0 .75em;
 white-space: nowrap;
}
.nav li :link, .nav li :visited { padding: 0 .5em }
.nav li.last { border-right: none }
/* Main navigation bar */
#mainnav {
 background: #f7f7f7 url(../topbar_gradient.png) top left;
 border: 1px solid #000;
 font: normal 10px verdana,'Bitstream Vera Sans',helvetica,arial,sans-serif;
 height: 1.6em;
 margin: .66em 0 .33em;
}
#mainnav ul { float: right; padding: 0 }
#mainnav li { border-right: none; padding: 0 }
#mainnav :link, #mainnav :visited {
 background: url(../dots.gif) top left no-repeat;
 border-left: 1px solid #555;
 border-right: 1px solid #fff;
 border-bottom: none;
 color: #000;
 /* Hide from IE/Mac \*/
 display: block;
 float: left;
 /* Unhide */
 line-height: 1.4em;
 padding: .1em 20px;
}
#mainnav .active:link, #mainnav .active:visited {
 background: #333 url(../topbar_gradient2.png) top left repeat-x;
 color: #eee;
 border-top: none;
 border-right: none !important;
 border-right: 1px solid #000;
 font-weight: bold;
}
#mainnav :link:hover, #mainnav :visited:hover {
 background-color: #ccc;
 border-right: 1px solid #ddd;
}
/* Context-dependent navigation links */
#ctxtnav li ul {
 background: #f7f7f7;
 color: #ccc;
 border: 1px solid;
 padding: 0;
 display: inline;
 margin: 0;
}
#ctxtnav li li { padding: 0; }
#ctxtnav li li :link, #ctxtnav li li :visited { padding: 0 1em }
#ctxtnav li li :link:hover, #ctxtnav li li :visited:hover {
 background: #bba;
 color: #fff;
}

/* Alternate links */
#altlinks { clear: both; text-align: center }
#altlinks h3 { font-size: 12px; letter-spacing: normal; margin: 0 }
#altlinks ul { list-style: none; margin: 0; padding: 0 0 1em }
#altlinks li {
 border-right: 1px solid #d7d7d7;
 display: inline;
 font-size: 11px;
 line-height: 16px;
 padding: 0 1em;
 white-space: nowrap;
}
#altlinks li.last { border-right: none }
#altlinks li :link, #altlinks li :visited {
 background-position: 0 -1px;
 background-repeat: no-repeat;
 border: none;
}
#altlinks li a.ics { background-image: url(../ics.png); padding-left: 22px }
#altlinks li a.rss { background-image: url(../xml.png); padding-left: 42px }

/* Footer */
#footer {
  clear: both;
  color: #bbb;
  font-size: 10px;
  border-top: 1px solid;
  height: 31px;
  padding: .25em 0;
}
#footer :link, #footer :visited { color: #bbb; }
#footer hr { display: none }
#footer #tracpowered { border: 0; float: left }
#footer #tracpowered:hover { background: transparent }
#footer p { margin: 0 }
#footer p.left {
  float: left;
  margin-left: 1em;
  padding: 0 1em;
  border-left: 1px solid #d7d7d7;
  border-right: 1px solid #d7d7d7;
}
#footer p.right {
  float: right;
  text-align: right;
}

#content { padding-bottom: 2em; position: relative }

#help {
 clear: both;
 color: #999;
 font-size: 90%;
 margin: 1em;
 text-align: right;
}
#help :link, #help :visited { cursor: help }
#help hr { display: none }

/* Page preferences form */
#prefs {
 background: #f7f7f0;
 border: 1px outset #998;
 float: right;
 font-size: 9px;
 padding: .8em;
 position: relative;
 margin: 0 1em 1em;
}
* html #prefs { width: 26em } /* Set width only for IE */
#prefs input, #prefs select { font-size: 9px; vertical-align: middle }
#prefs fieldset { border: none; margin: .5em; padding: 0 }
#prefs fieldset legend {
 background: transparent;
 color: #000;
 font-size: 9px;
 font-weight: normal;
 margin: 0 0 0 -1.5em;
 padding: 0;
}
#prefs .buttons { text-align: right }

/* Wiki */
a.missing:link,a.missing:visited { background: #fafaf0; color: #998 }
a.missing:hover { color: #000; }

#content.wiki { line-height: 140% }
.wikitoolbar {
 border: solid #d7d7d7;
 border-width: 1px 1px 1px 0;
 float: left;
 height: 18px;
}
.wikitoolbar :link, .wikitoolbar :visited {
 background: transparent url(../edit_toolbar.png) no-repeat;
 border: 1px solid #fff;
 border-left-color: #d7d7d7;
 cursor: default;
 display: block;
 float: left;
 width: 24px;
 height: 16px;
}
.wikitoolbar :link:hover, .wikitoolbar :visited:hover {
 background-color: transparent;
 border: 1px solid #fb2;
}
.wikitoolbar a#em { background-position: 0 0 }
.wikitoolbar a#strong { background-position: 0 -16px }
.wikitoolbar a#heading { background-position: 0 -32px }
.wikitoolbar a#link { background-position: 0 -48px }
.wikitoolbar a#code { background-position: 0 -64px }
.wikitoolbar a#hr { background-position: 0 -80px }

/* Styles for the form for adding attachments. */
#attachment .field { margin-top: 1.3em }
#attachment label { padding-left: .2em }
#attachment fieldset { margin-top: 2em }
#attachment fieldset .field { float: left; margin: 0 1em .5em 0 }
#attachment br { clear: left }

/* Styles for tabular listings such as those used for displaying directory
   contents and report results. */
table.listing {
 clear: both;
 border-bottom: 1px solid #d7d7d7;
 border-collapse: collapse;
 border-spacing: 0;
 margin-top: 1em;
 width: 100%;
}
table.listing th { text-align: left; padding: 0 1em .1em 0; font-size: 12px }
table.listing thead { background: #f7f7f0 }
table.listing thead th {
 border: 1px solid #d7d7d7;
 border-bottom-color: #999;
 font-size: 11px;
 font-weight: bold;
 padding: 2px .5em;
 vertical-align: bottom;
}
table.listing thead th :link:hover, table.listing thead th :visited:hover {
 background-color: transparent;
}
table.listing thead th a { border: none; padding-right: 12px }
table.listing th.asc a, table.listing th.desc a { font-weight: bold }
table.listing th.asc a, table.listing th.desc a {
 background-position: 100% 50%;
 background-repeat: no-repeat;
}
table.listing th.asc a { background-image: url(../asc.png) }
table.listing th.desc a { background-image: url(../desc.png) }
table.listing tbody td, table.listing tbody th {
 border: 1px dotted #ddd;
 padding: .33em .5em;
 vertical-align: top;
}
table.listing tbody td a:hover, table.listing tbody th a:hover {
 background-color: transparent;
}
table.listing tbody tr { border-top: 1px solid #ddd }
table.listing tbody tr.even { background-color: #fcfcfc }
table.listing tbody tr.odd { background-color: #f7f7f7 }
table.listing tbody tr:hover { background: #eed !important }

.wikipage p { margin-left: 1em }
pre.wiki, pre.literal-block {
 background: #f7f7f7;
 border: 1px solid #d7d7d7;
 margin: 1em 1.75em;
 padding: .25em;
 overflow: auto;
}
table.wiki {
 border: 2px solid #ccc;
 border-collapse: collapse;
 border-spacing: 0;
}
table.wiki td { border: 1px solid #ccc;  padding: .1em .25em; }

/* Styles for the error page (and rst errors) */
#content.error .message, div.system-message {
 background: #fdc;
 border: 2px solid #d00;
 color: #500;
 padding: .5em;
 margin: 1em 0;
}
#content.error pre, div.system-message pre { margin-left: 1em; overflow: auto }
div.system-message p { margin: 0; }
div.system-message p.system-message-title { font-weight: bold; }

/* Styles for search word highlighting */
.searchword0 { background: #ff9 }
.searchword1 { background: #cfc }
.searchword2 { background: #cff }
.searchword3 { background: #ccf }
.searchword4 { background: #fcf }

@media print {
 #header, #altlinks, #footer { display: none }
 .nav, form { display: none }
}
"""
)

print sheet

