import pycrunchbase as pyc

cb = pyc.CrunchBase('f0172d1df1ca552457f0722ed6468809')

betterment = cb.organization('betterment')

print(betterment)

funding_rounds_summary = betterment.funding_rounds
print(funding_rounds_summary)

what_is_bt = betterment.description
where_is_bt = betterment.homepage_url
betterment_team = betterment.current_team
who_started_betterment = betterment.founders
in_the_news = betterment.news

print(what_is_bt)
print(where_is_bt)
print(betterment_team)
print(who_started_betterment)
print(in_the_news)

# Latest funding round - amount and date
round_uuid = funding_rounds_summary[len(funding_rounds_summary)-1].uuid
# print(round_uuid)

latest_round = cb.funding_round(round_uuid)
print(latest_round)



def founders(company):
    people = list()
    for founder in who_started_betterment:
        people.append(founder)

    people2 = list()
    for founder in people:
        founder = str(founder)
        bracket = founder.find('(')
        founder = founder[:bracket]
        founder = founder[:-1]
        people2.append(founder)

    for founder in people2:
        return(founder)

#print(founders('betterment'))
# print(a_founder)

# print(pyc.Investment)
