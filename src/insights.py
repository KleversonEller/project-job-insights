from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """

    jobs_list = read(path)

    types_jobs = {type_job["job_type"] for type_job in jobs_list}

    return list(types_jobs)


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """

    filter_jobs = [
        type_job for type_job in jobs if type_job["job_type"] == job_type
    ]
    return filter_jobs


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs_list = read(path)

    industries = {
        indust["industry"]
        for indust in jobs_list
        if len(indust["industry"]) > 0
    }

    return list(industries)


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filter_industry = [
        industries for industries in jobs if industries["industry"] == industry
    ]
    return filter_industry


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_list = read(path)

    salary = [
        float(value["max_salary"])
        for value in jobs_list
        if value["max_salary"].isdigit()
    ]

    return max(salary)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_list = read(path)

    salary = [
        float(value["min_salary"])
        for value in jobs_list
        if value["min_salary"].isdigit()
    ]

    return min(salary)


def aux_salary_range(job, salary):
    if int(job["max_salary"]) >= int(salary) >= int(job["min_salary"]):
        return True

    if int(job["max_salary"]) < int(job["min_salary"]):
        raise ValueError

    return False


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    try:
        return aux_salary_range(job, salary)

    except KeyError:
        raise ValueError

    except TypeError:
        raise ValueError


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    jobs_list = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)

        except ValueError:
            ...

    return jobs_list
