from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import auth_router, products_router

# Create database tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="University Assignment Web API (Python - FastAPI)",
    description="""
## API Documentation & Instructions

This Web API is built using **Python (FastAPI + SQLAlchemy)** as a direct replacement for ASP.NET Core Web API + Entity Framework Core.

### 🔐 How to test JWT Authentication via Swagger UI (Authorize Button):
1. Use **POST /auth/register** to create a new user account.
2. Use **POST /auth/login** to log in with your credentials and receive an `access_token`.
3. Copy the returned `access_token`.
4. Click the **Authorize** button at the top right of this Swagger page.
5. Paste your token in the Value box and click **Authorize**.
6. Now you can execute any of the protected CRUD operations under `/products`!
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth_router.router)
app.include_router(products_router.router)

@app.get("/", tags=["Root"])
def root_endpoint():
    return {
        "message": "Welcome to Python Web API Assignment!",
        "swagger_docs": "/docs",
        "redoc_docs": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
