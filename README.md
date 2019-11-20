# Interview Assignments
Code I've written for various job applications (company names have been removed).

## Company1
### Problem: Warmest N Days
There is a database of average daily temperatures for some location that spans multiple years. You will need to
write a function that will use this data and do some calculation on it. Data will be passed to your function as
an array of doubles with length M (one entry for each day). The goal of the function is to return the offset in
array that represents the warmest N successive days.

## Company2
### Write a python script that ingests data from one of the external vendor's data sources and combine that data with
our internal data set. This combined data set should allow data team members to compare the active users of the
different platforms. The script should finish in less than one hour.

### Requirements
The script can run in an environment with limited amounts of memory. The final solution should avoid reading all
the rows from either source at one time. For example, reading in 10% of database rows and 10% of API rows and then
do the matching would be acceptable. Reading in 100% of either source prior to matching would not be acceptable.
Pretend that the current date is 2017-02-02. There are references in the assignment that will confirm that as
the "current" date.

## Company3
### Protein Synthesis
Given a string containing codons, transcribe DNA to mRNA, starting when we see a start codon and ending when we see
a stop codon. 

## Company4
Various phone screen problems. 
- Variant of [Leetcode subdomain visit count](https://leetcode.com/problems/subdomain-visit-count/)
- We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order and no URL was visited more than once per person.

Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.
