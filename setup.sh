#!/bin/bash
export AUTH0_DOMAIN=anujafsnd-udacity.us.auth0.com
export ALGORITHMS='RS256'
export API_AUDIENCE=CastingAgency

# Tokens - These tokens are used for testing in Postman against Render app URL
export ASSISTANT='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdtOXJGLUNjNk1zVjlBRUpUM0tBUyJ9.eyJpc3MiOiJodHRwczovL2FudWphZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NTEwMDZhMjZlYTgyNWVmNGY1ZmFiNjYiLCJhdWQiOiJDYXN0aW5nQWdlbmN5IiwiaWF0IjoxNjk1OTg0MzM0LCJleHAiOjE2OTYwNzA3MzQsImF6cCI6ImdjMTU2eWtzOVFGSWNYZVc2OFA5SkpuMER4azlEd3V3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.fEcj13re3uksSiBK5vyKjzaR5sLf9fv0HjUE63cQrGtx8COuDk7Q7gKw0PsuSxMlD30VxFPftMZQorKauyx5ZIC3PXToKl3uuswbUKuIjU8pA0CFyT_uIXRwvVBHIZNKieusuRpScilRCgrJfYDmjeyuep6_vOYNXttrUk1lNCySKgA6Map7P7kpPpZA6FwLB0HKorkBK68y1HwZLcTsYEfxz3sM-jO9KFTfJh3iAA6YQV1Dghf7uiO61vOUOOZKblk_em8fPgAfLdu8S_J_yT0lUtaScZfi22AtKD66J9mVtwCdlAsun8FMtMhBmWwjlp35CXyCiMHZ-PXorUWBUg'
export DIRECTOR='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdtOXJGLUNjNk1zVjlBRUpUM0tBUyJ9.eyJpc3MiOiJodHRwczovL2FudWphZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NTEwMDZkOTcwZDNjZmU3ZWM4MmMxZGEiLCJhdWQiOiJDYXN0aW5nQWdlbmN5IiwiaWF0IjoxNjk1OTk0MTY4LCJleHAiOjE2OTYwODA1NjgsImF6cCI6ImdjMTU2eWtzOVFGSWNYZVc2OFA5SkpuMER4azlEd3V3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiZGVsZXRlOmFjdG9ycyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIiwidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.WSw1mrh-YCjGMXH97GXLyaYbvlxK_CJwLVAWvVztEQQjZD1hxQcgSoHqPTG_EPGdaZcLEkqrO9Q2ngunOZQyMZ32zWJT6L1QOt326y62tTZwkiDqoQP9d68tKwK5we9CHPJVxllkqs5yMPG0d_I7u92q-NPHbxls_GeEPOqqFS4f_Ymo9vxe8TPorn4HnvxOxe6J9FI3YD4k-tg2zdS_B5qHFa-CgvQ5FHsY_PgehmNLc-hQQDxFBLKglr1NOTYXbf39RhNgWHtc9J5SI2lEB1Cv-2ck8Np_KOSYyqnuyKnvCSAZie0mUZDYo4viq4FTghmNbtjPk1szDQHH9BNL-g'
export PRODUCER='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdtOXJGLUNjNk1zVjlBRUpUM0tBUyJ9.eyJpc3MiOiJodHRwczovL2FudWphZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NTEwMDZmMzdmZDQ4YWU0OTEwZTJkOTYiLCJhdWQiOiJDYXN0aW5nQWdlbmN5IiwiaWF0IjoxNjk1OTk0MjY3LCJleHAiOjE2OTYwODA2NjcsImF6cCI6ImdjMTU2eWtzOVFGSWNYZVc2OFA5SkpuMER4azlEd3V3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiYWRkOm1vdmllcyIsImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.DC-jr6a3MZPM71m1Vjlkm06BBHiEUV6S1TOVSfNdlH-F9-2I9WWKRcFxayT3y6G2Ji2xxC2Mae8iPubhUXkTdByvHKWZ4y0Ba4GUGSLaTKNDU_OyHG9VLM4TH7Qe_QlvXHXZYqN6fDPSI3ZN-xXWV_SugtkpC7hMOKlROngnZVobaa21l7JydDJBfLC8q_qeeq6v4GC7MrPE9IGzmOi_RXzL5ogQk1iBHjZoM6cYkxbCyoFHwtbrVQx3SOY6Ii6mjleH_xu2mvJo9FDhO3PifLBph_ZWtxEEOl-RAnFi5hs2cA-PmQha-P08lm-NHAL5M4ePNvo006J-THsVDqfuYw'


export EXCITED="true"
echo "setup.sh script executed successfully!"

