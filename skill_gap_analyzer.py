import re

# Load files
with open("resume.txt", "r") as f:
    resume_text = f.read().lower()

with open("job_description.txt", "r") as f:
    job_text = f.read().lower()

# Skill list (can expand)
skills = [
    "python", "sql", "power bi", "excel", "machine learning",
    "statistics", "tableau", "pandas", "numpy",
    "data analysis", "data visualization", "R"
]

# Extract skills
resume_skills = {skill for skill in skills if skill in resume_text}
job_skills = {skill for skill in skills if skill in job_text}

# Skill gap analysis
matched_skills = resume_skills.intersection(job_skills)
missing_skills = job_skills - resume_skills

match_percentage = (len(matched_skills) / len(job_skills)) * 100

# Output
print("✅ Matched Skills:")
for skill in matched_skills:
    print("-", skill)

print("\n❌ Missing Skills:")
for skill in missing_skills:
    print("-", skill)

print(f"\n📊 Resume Match Percentage: {match_percentage:.2f}%")
