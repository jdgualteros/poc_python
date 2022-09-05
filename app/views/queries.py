
sql = {"quarter": """select department, job,
	count(case cuarter when 1 then cuarter  end) as "Q1",
	count(case cuarter when 2 then cuarter  end) as "Q2",
	count(case cuarter when 3 then cuarter  end) as "Q3",
	count(case cuarter when 4 then cuarter  end) as "Q4"
	from
	(
		select d.department, j.job, extract (quarter from TO_TIMESTAMP(
		    e.datetime ,'YYYY-MM-DD TO:MI:SS')) as cuarter
		from "employees" e
			inner join "departments" d
			on e.department_id = d.id
			inner join "jobs" j
			on e.job_id = j.id
			where substring(e.datetime,1,4) = '2021') as temp
	group by department, job""",

        "media": """select d.department, j.job, avg(e.id) as hired 
            from "employees" e
                inner join "departments" d
                on e.department_id = d.id
                inner join "jobs" j
                on e.job_id = j.id
                where substring(e.datetime,1,4) = '2021'
                group by j.job, d.department """}
