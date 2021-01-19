e
The header is subject to change so you typically have to regenerate the default header when upgrading to a newer version of doxygen. The following markers have a special meaning inside the header and footer:
$title
will be replaced with the title of the page.
$datetime
will be replaced with current the date and time.
$date
will be replaced with the current date.
$year
will be replaces with the current year.
$doxygenversion
will be replaced with the version of doxygen
$projectname
will be replaced with the name of the project (see PROJECT_NAME)
$projectnumber
will be replaced with the project number (see PROJECT_NUMBER)
$projectbrief
will be replaced with the project brief description (see PROJECT_BRIEF)
$projectlogo
will be replaced with the project logo (see PROJECT_LOGO)
$treeview
will be replaced with links to the javascript and style sheets needed for the navigation tree (or an empty string when GENERATE_TREEVIEW is disabled).
$search
will be replaced with a links to the javascript and style sheets needed for the search engine (or an empty string when SEARCHENGINE is disabled).
$mathjax
will be replaced with a links to the javascript and style sheets needed for the MathJax feature (or an empty string when USE_MATHJAX is disabled).
$relpath^
If CREATE_SUBDIRS is enabled, the command $relpath^ can be used to produce a relative path to the root of the HTML output directory, e.g. use $relpath^doxygen.css, to refer to the standard style sheet.
