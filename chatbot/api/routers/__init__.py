from chatbot.api.routers import chatbot_routes


def include_routers(app):
    app.include_router(chatbot_routes.router)

