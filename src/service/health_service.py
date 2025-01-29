from datetime import datetime

class HealthService:
    @staticmethod
    async def check_health():
        return {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "version": "1.0.0"
        }