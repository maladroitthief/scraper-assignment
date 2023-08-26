# scraper-assignment

## Assumptions

- Could probably use crunchbase for public/aquired
    - Easiest to use web domain to verify a match
    - Monthly limit, disregard

- Lightspeed does not have any of those fields


## Architecture


## Data-Structures


## Testing


---

Write a program that scrapes an investor website and extracts a list of domains for all their portfolio companies.

## Constraints:

Use python3

Use https://github.com/scrapy/scrapy framework to implement the scraper

Use git to manage your code

Ignore companies that are public or acquired, but keep their active investments

Include a README file that explains the following: Assumptions, Architecture, Data structures, Testing methodology

Feel free to use additional third-party python libraries and other systems if it helps you solve the problem.

Input websites are:

https://www.amplifypartners.com/portfolio

https://lsvp.com/portfolio/

Expected Results:

Your code should generate results that look like:

```json
{
    "amplifypartners.com": [
        "actioniq.com",
        "anchorage.com",
        "anyscale.com",
        "archera.ai",
        "authzed.com",
        ...
    ],
    "lsvp.com": [
        "1047games.com",
        "1password.com",
        "2boss.cn",
        "51hitech.com",
        "abatatx.com",
        "abstract.com",
        "...."
    ]
}
```

## Bonus:

Extend the scraper to extract the domain and company name, then write a simple REST webservice using Flask that implements an endpoint for an autocomplete feature on the company name and returns associated domains and investors information.

Write your own REST endpoint that implements an interesting feature based on the scraped data.

Write a Dockerfile that creates a Docker image of your webservice.
