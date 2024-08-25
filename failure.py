import streamlit_shadcn_ui as ui
trigger_btn = ui.button(text="Trigger Button", key="trigger_btn")

ui.alert_dialog(show=trigger_btn, title="Failure", description="You failed to complete the assignment before class. Next time maybe use the AI assistant", confirm_label="Try Again", cancel_label="I give up", key="alert_dialog1")
