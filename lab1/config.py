import enum

class Job(enum.Enum):
    TO_STAR = 'to_star'
    TO_SLASH = 'to_slash'



def change_string_to_char(str_to_update, char: str):
    return char.join(str_to_update)

JOB_TO_FUNCTION = {
    Job.TO_STAR: lambda x: change_string_to_char(x, '*'),
    Job.TO_SLASH: lambda x: change_string_to_char(x, '/')
}
