from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Assessment(Base):
    __tablename__ = "assessments"

    assessment_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    total_epds_score = Column(Integer, nullable=False)
    depression_level = Column(String, nullable=False)

    answers = relationship("EPDSAnswer", back_populates="assessment")
