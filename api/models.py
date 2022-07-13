# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attachments(models.Model):
    schedule = models.ForeignKey('Schedules', models.DO_NOTHING)
    filepath = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachments'


class Audits(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_type = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    event = models.CharField(max_length=255)
    auditable_type = models.CharField(max_length=255)
    auditable_id = models.PositiveBigIntegerField()
    old_values = models.TextField(blank=True, null=True)
    new_values = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.CharField(max_length=1023, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audits'


class Categories(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    belongs_to = models.CharField(max_length=255, blank=True, null=True)
    subscriber_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'categories'


class CrewEmployees(models.Model):
    crew = models.ForeignKey('Crews', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crew_employees'


class Crews(models.Model):
    subscriber = models.ForeignKey('Subscribers', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    is_archive = models.IntegerField()
    is_manual = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'crews'


class Features(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'features'


class Inventories(models.Model):
    parent = models.ForeignKey('self', models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    metric = models.ForeignKey('Metrics', models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_assembly = models.IntegerField()
    subscriber_id = models.PositiveIntegerField()
    main_image_id = models.IntegerField(blank=True, null=True)
    low_inventory_warning = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventories'


class InventoryAssemblies(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    inventory = models.ForeignKey(Inventories, models.DO_NOTHING, related_name='inventory_assemblies')
    part = models.ForeignKey(Inventories, models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_assemblies'


class InventoryImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    inventory_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_image'


class InventoryPicklists(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    picklist = models.ForeignKey('Picklists', models.DO_NOTHING, blank=True, null=True)
    inventory = models.ForeignKey(Inventories, models.CASCADE)
    location = models.ForeignKey('Locations', models.DO_NOTHING)
    reserved_stock = models.IntegerField()
    used_stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inventory_picklists'


class InventorySkus(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    inventory = models.ForeignKey(Inventories, models.DO_NOTHING)
    code = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'inventory_skus'


class InventoryStockMovements(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    stock = models.ForeignKey('InventoryStocks', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    before = models.DecimalField(max_digits=8, decimal_places=2)
    after = models.DecimalField(max_digits=8, decimal_places=2)
    cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_stock_movements'


class InventoryStocks(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    inventory = models.ForeignKey(Inventories, models.DO_NOTHING)
    location = models.ForeignKey('Locations', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    aisle = models.CharField(max_length=255, blank=True, null=True)
    row = models.CharField(max_length=255, blank=True, null=True)
    bin = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_stocks'
        unique_together = (('inventory', 'location'),)


class InventorySuppliers(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    inventory = models.ForeignKey(Inventories, models.DO_NOTHING)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inventory_suppliers'


class InventoryTransactionHistories(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    transaction = models.ForeignKey('InventoryTransactions', models.DO_NOTHING)
    state_before = models.CharField(max_length=255)
    state_after = models.CharField(max_length=255)
    quantity_before = models.CharField(max_length=255)
    quantity_after = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'inventory_transaction_histories'


class InventoryTransactions(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    stock = models.ForeignKey(InventoryStocks, models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    subscriber_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'inventory_transactions'


class Locations(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    belongs_to = models.CharField(max_length=255, blank=True, null=True)
    subscriber_id = models.PositiveIntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class Metrics(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    subscriber_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'metrics'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class ParentTasks(models.Model):
    parent_task = models.ForeignKey('Tasks', models.DO_NOTHING)
    child_task = models.ForeignKey('Tasks', models.DO_NOTHING, related_name='parent_tasks')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parent_tasks'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    subdomain = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class Picklists(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    subscriber = models.ForeignKey('Subscribers', models.DO_NOTHING)
    schedule = models.ForeignKey('Schedules', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    task = models.ForeignKey('Tasks', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picklists'


class Roles(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Schedules(models.Model):
    subscriber = models.ForeignKey('Subscribers', models.DO_NOTHING)
    builder = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    lot = models.CharField(max_length=255, blank=True, null=True)
    block = models.CharField(max_length=255, blank=True, null=True)
    subdivision = models.CharField(max_length=255, blank=True, null=True)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    elevation = models.CharField(max_length=255, blank=True, null=True)
    permit_number = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    archive = models.IntegerField()
    is_schedule = models.IntegerField()
    attachment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedules'


class StripeHooks(models.Model):
    subscriber_id = models.IntegerField(blank=True, null=True)
    customer_id = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    payload = models.JSONField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stripe_hooks'


class SubscriberFeatureAccess(models.Model):
    id = models.BigAutoField(primary_key=True)
    subscriber = models.ForeignKey('Subscribers', models.DO_NOTHING)
    feature = models.ForeignKey(Features, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriber_feature_access'


class Subscribers(models.Model):
    company_name = models.CharField(max_length=255)
    company_logo = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=255, blank=True, null=True)
    subdomain = models.CharField(unique=True, max_length=128)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    wc_subscription_id = models.IntegerField(blank=True, null=True)
    customer_id = models.CharField(max_length=255, blank=True, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    active = models.IntegerField()
    status = models.CharField(max_length=255, blank=True, null=True)
    num_users_availed = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    enable_publish = models.IntegerField(blank=True, null=True)
    publish_time = models.TimeField(blank=True, null=True)
    timezone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscribers'


class SubscriptionHistories(models.Model):
    subscriber = models.ForeignKey(Subscribers, models.DO_NOTHING)
    start = models.DateTimeField()
    end = models.DateTimeField()
    price = models.FloatField(blank=True, null=True)
    subscription_plan = models.ForeignKey('SubscriptionPlans', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_histories'


class SubscriptionPlans(models.Model):
    product_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    price = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    min_users = models.IntegerField(blank=True, null=True)
    max_users = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_plans'


class SubscriptionPriceLogs(models.Model):
    description = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    price = models.FloatField()
    subscription_plan = models.ForeignKey(SubscriptionPlans, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_price_logs'


class Subscriptions(models.Model):
    subscriber_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    braintree_id = models.CharField(max_length=255)
    braintree_plan = models.CharField(max_length=255)
    quantity = models.IntegerField()
    trial_ends_at = models.DateTimeField(blank=True, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriptions'


class Suppliers(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    contact_title = models.CharField(max_length=255, blank=True, null=True)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=255, blank=True, null=True)
    contact_fax = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.CharField(max_length=255, blank=True, null=True)
    subscriber_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'suppliers'


class Taggables(models.Model):
    tag = models.ForeignKey('Tags', models.DO_NOTHING)
    taggable_id = models.PositiveIntegerField()
    taggable_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'taggables'


class Tags(models.Model):
    name = models.JSONField()
    slug = models.JSONField()
    type = models.CharField(max_length=255, blank=True, null=True)
    order_column = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


class TaskEmployees(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_id = models.PositiveIntegerField()
    task_id = models.PositiveIntegerField()
    role = models.CharField(max_length=11)
    crew_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_employees'


class Tasks(models.Model):
    schedule = models.ForeignKey(Schedules, models.DO_NOTHING)
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.CharField(max_length=11)
    complete_start = models.DateTimeField(blank=True, null=True)
    complete_end = models.DateTimeField(blank=True, null=True)
    crew = models.ForeignKey(Crews, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    task_logged = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=14)

    class Meta:
        managed = False
        db_table = 'tasks'


class TimeOff(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    subscriber_id = models.PositiveBigIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    all_day = models.IntegerField()
    reason = models.TextField()
    status = models.CharField(max_length=8)
    processed_by = models.PositiveBigIntegerField()
    is_archive = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_off'


class TimeTrackers(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    start = models.DateTimeField()
    end = models.DateTimeField()
    break_field = models.IntegerField(db_column='break')  # Field renamed because it was a Python reserved word.
    status = models.CharField(max_length=12)
    approval_date = models.DateTimeField()
    approved_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_trackers'


class UserImages(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)
    image_file = models.CharField(max_length=255)
    image_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_images'


class UserRoles(models.Model):
    role = models.ForeignKey(Roles, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_roles'


class Users(models.Model):
    employee_no = models.IntegerField(blank=True, null=True)
    subscriber = models.ForeignKey(Subscribers, models.DO_NOTHING, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=255, blank=True, null=True)
    pay_rate = models.FloatField(blank=True, null=True)
    last_raise = models.DateTimeField(blank=True, null=True)
    termination = models.DateTimeField(blank=True, null=True)
    archive = models.IntegerField(blank=True, null=True)
    site_wide = models.IntegerField(blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

