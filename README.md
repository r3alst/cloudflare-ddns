## Cloudflare DDNS

### Development env setup

1. Create .env file

   ```shell
   cp .env.example .env
   ```

2. Go to [Cloudflare API Token](https://dash.cloudflare.com/profile/api-tokens).

3. Click "Create Token" button and select _Edit zone DNS_ Template

4. Update generated Token in `.env` file against _CLOUDFLARE_API_TOKEN_

5. Go to your website page on Cloudflare. In Dashboard search for _Zone ID_

6. Update _Zone ID_ in `.env` file against _CLOUDFLARE_ZONE_ID_

7. Add Random/Reserved DNS name against _DDNS_RECORD_NAME_ in `.env`

8. Install virtualenv if not present on your machine

   ```shell
   pip3 install virtualenv
   ```

9. Create virtualenv and install deps

   ```shell
   virtualenv venv
   source venv/bin/activate
   pip3 install -r requirements.txt
   ```

### Docker Setup:

1. Install Docker
2. Run following commands

   ```shell
   docker compose up -d
   ```

### To Run script without Docker

```shell
source venv/bin/activate
python main.py
```
