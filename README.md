#Check any Google Play Payment

To use this source you must retrieve [payment token](http://developer.android.com/google/play/billing/billing_reference.html) from google play purchases.


##Installation

Create virtual env, clone project and install prerequisites

```
virtualenv .
git clone https://github.com/Agasper/django-google-play-check-payment.git project
source ./bin/activate
pip install -r ./project/req.txt
```

##Account, Keys and other stuff

* Go to https://console.developers.google.com/project
* Create new project
* Go to ```Project -> APIS & AUTH -> APIs``` and enable ```Google Play Android Developer API```
* Go to ```Project -> APIS & AUTH -> Credentials``` and create new Client ID Service Account
* Generate and download new P12 key
* Rename this key to `key.p12` and put into ```keys``` directory
* Go to https://play.google.com/apps/publish/ , next ```Settings -> Accounts and roles -> Invite user``` and invite user (e-mail) from your service account above.
* Give him financial role

##Using

This is test example, to use this on production server - use nginx+gunicorn or nginx+<what u prefer for backend>

```
./manage.py runserver 0.0.0.0:8000
```

Request:

```
http://host:8000/license?package=<package_name>&sku=<product_id>&service=<account>&key=<key>&token=<token>
```
where:

* package - is your application package name, ex. ```net.solargames.dungeonexplorer2```
* product_id - is your IAP name, ex. ```net.solargames.dungeonexplorer2.gold```
* account - is your service account email
* key - key filename from ```keys``` directory without extension, ex. ```key```
* token - your purchase token from the beginning of this manual

Response:

If purchase valid, you will see:
```
<?xml version="1.0" encoding="UTF-8"?><result consumptionState="1" purchaseState="0" purchaseTime="1405003881937" status="0" />
```
otherwise:
```
<?xml version="1.0" encoding="UTF-8"?><result message="Invalid Value" status="1" />
```
