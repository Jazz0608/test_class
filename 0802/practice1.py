# practice1.py — 複雜範例：學生成績管理系統

# ── 1. 資料定義 ──────────────────────────────────────────────────────────────
students = [
    {"name": "小明", "scores": [85, 92, 78, 90]},
    {"name": "小華", "scores": [70, 65, 80, 75]},
    {"name": "小美", "scores": [95, 88, 92, 96]},
    {"name": "小強", "scores": [60, 55, 70, 65]},
]

# ── 2. 函式定義 ──────────────────────────────────────────────────────────────
def calculate_average(scores: list[int]) -> float:
    """計算成績平均"""
    return sum(scores) / len(scores)


def grade(average: float) -> str:
    """根據平均分給出等第"""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# ── 3. 類別定義 ──────────────────────────────────────────────────────────────
class Student:
    def __init__(self, name: str, scores: list[int]):
        self.name = name
        self.scores = scores
        self.average = calculate_average(scores)
        self.grade = grade(self.average)

    def __repr__(self) -> str:
        return f"Student({self.name!r}, avg={self.average:.1f}, grade={self.grade})"

    def highest(self) -> int:
        return max(self.scores)

    def lowest(self) -> int:
        return min(self.scores)


# ── 4. 建立物件清單 ──────────────────────────────────────────────────────────
roster = [Student(s["name"], s["scores"]) for s in students]

# ── 5. 顯示每位學生成績報告 ──────────────────────────────────────────────────
print("=" * 40)
print(f"{'姓名':<6} {'平均':>6} {'等第':>4} {'最高':>4} {'最低':>4}")
print("-" * 40)
for s in roster:
    print(f"{s.name:<6} {s.average:>6.1f} {s.grade:>4} {s.highest():>4} {s.lowest():>4}")
print("=" * 40)

# ── 6. 找出最高分與最低分學生 ────────────────────────────────────────────────
top = max(roster, key=lambda s: s.average)
bottom = min(roster, key=lambda s: s.average)
print(f"\n🏆 最高平均：{top.name}（{top.average:.1f}）")
print(f"📉 最低平均：{bottom.name}（{bottom.average:.1f}）")

# ── 7. 等第統計 ──────────────────────────────────────────────────────────────
from collections import Counter

grade_counts = Counter(s.grade for s in roster)
print("\n等第分布：")
for g in ["A", "B", "C", "D", "F"]:
    bar = "█" * grade_counts.get(g, 0)
    print(f"  {g}: {bar} ({grade_counts.get(g, 0)} 人)")
