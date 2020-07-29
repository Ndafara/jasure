import lambda_router
import structlog

config_template = {
    "REGION": {"required": True},
    "ENVIRONMENT": {"required": False},
}
config = lambda_router.config.Config()
config.load_from_environment(template=config_template)

app = lambda_router.App(name="daily_scheduled", config=config)
app.logger = structlog.get_logger()


@app.route()
def perform_daily(event):
    app.logger.info("Starting daily task")
    app.logger.info("Finished daily task")
    return True
