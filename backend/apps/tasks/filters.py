from django_filters import rest_framework as filters


class TaskFilter(filters.FilterSet):
    task_done = filters.BooleanFilter(field_name='status')

