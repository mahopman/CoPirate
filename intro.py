import streamlit_shadcn_ui as ui
trigger_btn = ui.button(text="Trigger Button", key="trigger_btn")

ui.alert_dialog(show=trigger_btn, title="Hello", description="You are a university student taking an intro to programming", confirm_label="OK", cancel_label="Cancel", key="alert_dialog1")
