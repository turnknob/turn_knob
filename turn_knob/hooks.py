app_name = "turn_knob"
app_title = "turnKnob"
app_publisher = "Raghav Ruia & others"
app_description = "TURN KNOB is a free, city-wide directory that helps artists effortlessly find and filter recording studios by gear, space, and vibe - all while giving studios a simple way to get discovered and fully booked."
app_email = "raghavruia.dev@gmail.com"
app_license = "agpl-3.0"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
add_to_apps_screen = [
	{
		"name": "turn_knob",
		"logo": "/assets/turn_knob/logo.png",
		"title": "turnKnob",
		"route": "/turn_knob",
		"has_permission": "turn_knob.api.permission.has_app_permission"
	}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/turn_knob/css/turn_knob.css"
# app_include_js = "/assets/turn_knob/js/turn_knob.js"

# include js, css files in header of web template
# web_include_css = "/assets/turn_knob/css/turn_knob.css"
# web_include_js = "/assets/turn_knob/js/turn_knob.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "turn_knob/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "turn_knob/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "turn_knob.utils.jinja_methods",
# 	"filters": "turn_knob.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "turn_knob.install.before_install"
# after_install = "turn_knob.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "turn_knob.uninstall.before_uninstall"
# after_uninstall = "turn_knob.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "turn_knob.utils.before_app_install"
# after_app_install = "turn_knob.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "turn_knob.utils.before_app_uninstall"
# after_app_uninstall = "turn_knob.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "turn_knob.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"turn_knob.tasks.all"
# 	],
# 	"daily": [
# 		"turn_knob.tasks.daily"
# 	],
# 	"hourly": [
# 		"turn_knob.tasks.hourly"
# 	],
# 	"weekly": [
# 		"turn_knob.tasks.weekly"
# 	],
# 	"monthly": [
# 		"turn_knob.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "turn_knob.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "turn_knob.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "turn_knob.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["turn_knob.utils.before_request"]
# after_request = ["turn_knob.utils.after_request"]

# Job Events
# ----------
# before_job = ["turn_knob.utils.before_job"]
# after_job = ["turn_knob.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"turn_knob.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

