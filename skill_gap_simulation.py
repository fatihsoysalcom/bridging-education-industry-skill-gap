import random

# Represents skills required by the industry
class IndustrySkills:
    def __init__(self):
        self.required_skills = {
            "Python": 0.8,
            "Data Analysis": 0.7,
            "Machine Learning": 0.6,
            "Cloud Computing": 0.5,
            "Cybersecurity": 0.4
        }

    def get_required_skill_level(self, skill_name):
        return self.required_skills.get(skill_name, 0.0)

# Represents skills possessed by graduates
class GraduateSkills:
    def __init__(self, name):
        self.name = name
        self.possessed_skills = {}
        # Simulate some basic skills
        self.possessed_skills["Python"] = random.uniform(0.3, 0.7)
        self.possessed_skills["Data Analysis"] = random.uniform(0.2, 0.6)
        self.possessed_skills["Problem Solving"] = random.uniform(0.5, 0.9)

    def get_possessed_skill_level(self, skill_name):
        return self.possessed_skills.get(skill_name, 0.0)

    def assess_skill_gap(self, industry_skills):
        gaps = {}
        total_gap_score = 0.0
        for skill, required_level in industry_skills.required_skills.items():
            possessed_level = self.get_possessed_skill_level(skill)
            gap = max(0, required_level - possessed_level) # Gap is only positive
            gaps[skill] = gap
            total_gap_score += gap
        return gaps, total_gap_score / len(industry_skills.required_skills) if industry_skills.required_skills else 0

# --- Simulation --- 

print("--- Skill Gap Simulation ---")

# Define industry needs
industry = IndustrySkills()
print("\nIndustry Required Skills (Target Levels):")
for skill, level in industry.required_skills.items():
    print(f"- {skill}: {level:.2f}")

# Simulate a few graduates
graduates = [
    GraduateSkills("Alice"),
    GraduateSkills("Bob"),
    GraduateSkills("Charlie")
]

print("\nAssessing Graduates:")
for grad in graduates:
    print(f"\nGraduate: {grad.name}")
    # Assess the skill gap for each graduate against industry needs
    gaps, avg_gap = grad.assess_skill_gap(industry)
    print("  Skill Gaps:")
    for skill, gap in gaps.items():
        print(f"    - {skill}: {gap:.2f} (Required: {industry.get_required_skill_level(skill):.2f}, Possessed: {grad.get_possessed_skill_level(skill):.2f})")
    print(f"  Average Skill Gap Score: {avg_gap:.2f}")

    # Simple recommendation based on gap
    if avg_gap > 0.3:
        print("  Recommendation: Further training or upskilling needed in key areas.")
    else:
        print("  Recommendation: Well-aligned with industry needs.")
