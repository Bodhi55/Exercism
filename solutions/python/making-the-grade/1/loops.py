"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    round_scores_list = [round(score) for score in student_scores]

    return round_scores_list


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.
    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    failed_count = 0
    for index,score in enumerate(student_scores): 
        if score <= 40 : 
            failed_count += 1
            continue
    return failed_count
def above_threshold(student_scores, threshold):
    """Filter scores that are greater than or equal to the threshold."""
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Calculate the lower bounds for D, C, B, and A grades."""
    # We know failing is 40, so the range to split is from 41 to 'highest'
    step = (highest - 40) // 4
    return [41 + (i * step) for i in range(4)]


def student_ranking(student_scores, student_names):
    """Combine names and scores into a formatted ranking list."""
    rankings = []
    for index, name in enumerate(student_names):
        # index + 1 gives us the 1-based rank
        rankings.append(f"{index + 1}. {name}: {student_scores[index]}")
    return rankings


def perfect_score(student_info):
    """Find the first student with a score of 100."""
    for student in student_info:
        if student[1] == 100:
            return student
    return []