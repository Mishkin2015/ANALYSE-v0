from celery import task

from analytics import (update_DB_course_struct,
					   update_DB_course_spent_time,
					   update_DB_sort_course_homework,
					   update_DB_student_grades,
					   update_DB_course_section_accesses)
from analytics_jose import time_schedule
from data import get_courses_list
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from celeryHector import update_visualization_data


@task()
def update_DB_analytics():
	"""
	Update learning analytics DB data
	"""
	courses = get_courses_list()
	for course in courses:
		update_DB_course_struct(course.id)
		update_DB_student_grades(course.id)
		update_DB_course_spent_time(course.id)
		update_DB_sort_course_homework(course.id)
		update_DB_course_section_accesses(course.id)
		time_schedule(course.id)
		update_visualization_data(course.id)