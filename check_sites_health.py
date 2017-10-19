import datetime as dt

import requests
import whois


def load_urls4check(path_to_file):
    with open(path_to_file, "r", encoding='utf-8') as input_file:
        domain_list = input_file.readlines()
    return domain_list


def check_server_respond_with_200(url):
    ok_status_code = 200
    try:
        response_code = requests.get(url).status_code
        check_status = bool(response_code == ok_status_code)
    except requests.ConnectionError:
        response_code = 'ERR'
        check_status = False
    return response_code, check_status


def check_domain_expiration_date(domain_name, days_to_expire=30):
    whois_info = whois.whois(domain_name)
    if whois_info.expiration_date is None:
        expiration_date = None
        check_status = False
    elif type(whois_info.expiration_date) is list:
        expiration_date = whois_info.expiration_date[0]
        time_delta_in_days = (expiration_date - dt.datetime.now()).days
        check_status = bool(time_delta_in_days > days_to_expire)
    else:
        expiration_date = whois_info.expiration_date
        time_delta_in_days = (expiration_date - dt.datetime.now()).days
        check_status = bool(time_delta_in_days > days_to_expire)
    return expiration_date, check_status


def output_check_results_to_console(domains_list):
    for domain in domains_list:
        domain = domain.strip()
        domain_status_check = check_server_respond_with_200(
            'http://{}'.format(domain))
        domain_expiration_check = check_domain_expiration_date(domain)
        if not domain_expiration_check[1] or not domain_status_check[1]:
            check_resume = 'ATTENTION !!!'
        else:
            check_resume = 'OK'
        print(
            'Domain name: {:30} Response code: {} Expires date: {} '
            'Tests resume: {}'.format(domain,
                                      domain_status_check[0],
                                      domain_expiration_check[0],
                                      check_resume))


if __name__ == '__main__':
    domains_list = load_urls4check('domainslist.txt')
    output_check_results_to_console(domains_list)
