# Sample Test Cases

| Test | Example condition | Expected warning |
|---|---|---|
| 1 | URL contains `@` | @ symbol warning |
| 2 | URL longer than 100 characters | URL length warning |
| 3 | Hostname is an IPv4 address | IP hostname warning |
| 4 | Hostname has 5 or more labels | Hostname labels warning |
| 5 | Hostname contains `xn--` | Punycode warning |
| 6 | URL uses `http://` | HTTP scheme warning |

Run these tests locally before submitting. Record the actual results from your own computer.
