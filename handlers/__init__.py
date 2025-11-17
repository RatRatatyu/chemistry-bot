from .start import router as start_router
from .options import router as option_router
from .elements import router as elements_router
from .game import router as game_router

#Registers all module routers and attaches them to the main Dispatcher.
def register_handlers(dp):
    dp.include_router(start_router)
    dp.include_router(option_router)
    dp.include_router(elements_router)
    dp.include_router(game_router)
