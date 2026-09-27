from sqlalchemy import select

from app.db.session import SessionLocal
from app.models import Company, Contact, IntentSignal


def build_sample_companies() -> list[Company]:
    return [
        Company(
            name="Northwind Analytics",
            domain="northwind-analytics.example",
            website="https://northwind-analytics.example",
            industry="SaaS",
            description="Analytics platform for retail teams.",
            employee_count=80,
            country="United Kingdom",
            city="London",
            technologies=["HubSpot", "AWS", "React"],
            source="seed",
            contacts=[
                Contact(
                    first_name="Sarah",
                    last_name="Khan",
                    full_name="Sarah Khan",
                    job_title="COO",
                    seniority="c_suite",
                    email="sarah@northwind-analytics.example",
                    email_status="VALID",
                    email_confidence=95,
                    source="seed",
                ),
            ],
            signals=[
                IntentSignal(
                    type="HIRING",
                    description="12 open engineering positions on careers page.",
                    source_url="https://northwind-analytics.example/careers",
                    confidence="HIGH",
                    extra_data={"open_positions": 12},
                ),
                IntentSignal(
                    type="EXPANSION",
                    description="Announced a new office in Manchester.",
                    source_url="https://northwind-analytics.example/news",
                    confidence="MEDIUM",
                ),
            ],
        ),
        Company(
            name="Brightpath Digital",
            domain="brightpath-digital.example",
            website="https://brightpath-digital.example",
            industry="Marketing Agency",
            description=None,
            employee_count=35,
            country="United Kingdom",
            city="Manchester",
            source="seed",
            contacts=[
                Contact(
                    first_name="James",
                    last_name="Carter",
                    full_name="James Carter",
                    job_title="Founder",
                    seniority="founder",
                    email="james@brightpath-digital.example",
                    email_status="ACCEPT_ALL",
                    email_confidence=70,
                    source="seed",
                ),
            ],
            signals=[
                IntentSignal(
                    type="PRODUCT_LAUNCH",
                    description="Blog post announcing a new SEO service package.",
                    source_url="https://brightpath-digital.example/blog",
                    confidence="LOW",
                ),
            ],
        ),
        Company(
            name="Cedar Ledger",
            domain="cedar-ledger.example",
            website="https://cedar-ledger.example",
            industry="Fintech",
            description="Accounting automation for small businesses.",
            employee_count=150,
            country="United States",
            state="Texas",
            city="Austin",
            technologies=["Stripe", "Google Cloud"],
            source="seed",
            contacts=[
                Contact(
                    first_name="Maria",
                    last_name="Lopez",
                    full_name="Maria Lopez",
                    job_title="CTO",
                    seniority="c_suite",
                    email="maria@cedar-ledger.example",
                    email_status="UNKNOWN",
                    source="seed",
                ),
                Contact(
                    first_name="David",
                    last_name="Chen",
                    full_name="David Chen",
                    job_title="VP Operations",
                    seniority="vp",
                    email="d.chen@cedar-ledger.example",
                    email_status="INVALID",
                    email_confidence=10,
                    source="seed",
                ),
            ],
            signals=[
                IntentSignal(
                    type="FUNDING",
                    description="Press release announcing a Series A round.",
                    source_url="https://cedar-ledger.example/press",
                    confidence="HIGH",
                ),
            ],
        ),
    ]


def seed() -> None:
    db = SessionLocal()
    try:
        created = 0
        for company in build_sample_companies():
            exists = db.scalar(
                select(Company.id).where(Company.domain == company.domain)
            )
            if exists:
                print(f"Skipped (already exists): {company.name}")
                continue
            db.add(company)
            created += 1
            print(f"Added: {company.name}")
        db.commit()
        print(f"Done. {created} new companies added.")
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()