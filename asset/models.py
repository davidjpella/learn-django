from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'asset_locations'

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AssetType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'asset_types'

    def __str__(self):
        return self.name


class AssetStatus(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'asset_statuses'

    def __str__(self):
        return self.name


class Asset(models.Model):
    DEPRECIATION_METHOD_CHOICES = {
        'Straight-line': 'Straight-line',
        'Double declining balance': 'Double declining balance',
        'Units of production': 'Units of production',
        'Sum of years digits': 'Sum of years digits',
    }

    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255)
    purchase_date = models.DateField(null=True)
    purchase_cost = models.DecimalField(decimal_places=2, max_digits=10)
    depreciation_rate = models.DecimalField(decimal_places=2, max_digits=10)
    depreciation_method = models.CharField(max_length=55, choices=DEPRECIATION_METHOD_CHOICES)
    description = models.TextField(blank=True)
    warranty_expired_at = models.DateField(null=True)
    type = models.ForeignKey(
        AssetType, on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        AssetStatus, on_delete=models.CASCADE
    )
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'assets'

    def __str__(self):
        return self.name


class AssetFileType(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    asset = models.ForeignKey(
        Asset, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'asset_file_types'

    def __str__(self):
        return self.name


class Assignment(models.Model):
    assigned_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True)
    staff = models.ForeignKey(
        "staff.Staff", on_delete=models.CASCADE, null=True
    )
    asset = models.ForeignKey(
        Asset, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'asset_assignments'

    def __str__(self):
        return self.asset.name


class Retirement(models.Model):
    DISPOSAL_METHOD_CHOICES = {
        'Scrapping': {
            'description': 'Physically destroying the asset and disposing of the remains, often used for damaged or obsolete equipment.',
        },
        'Selling': {
            'description': 'Asset is sold to a third party (e.g., auction, internal sale, external buyer).',
        },
        'Trade-in': {
            'description': 'Asset is exchanged as part of the payment for a new one, often used for vehicles or IT hardware.',
        },
        'Donating': {
            'description': 'Giving the asset to a charity, school, or nonprofit. Often requires documentation for transparency.',
        },
        'Recycling': {
            'description': 'Sending the asset (or parts of it) to be recycled according to environmental regulations.',
        },
        'Return to vendor': {
            'description': 'Returning the asset to the original seller, typically under warranty, lease, or contract terms.',
        },
        'Internal reuse': {
            'description': 'Asset is no longer tracked as “assigned,” but is repurposed within the organization (e.g., moved to training/lab environment).',
        },
        'Lost/Stolen': {
            'description': 'Asset is no longer recoverable. Must be logged with appropriate documentation or investigation.',
        },
        'Burned/Damaged Beyond Repair': {
            'description': 'Used when assets are destroyed in fire, flood, or other irreversible accidents.',
        }
    }

    scrap_value = models.DecimalField(decimal_places=2, max_digits=10)
    disposal_method = models.CharField(max_length=255, choices=DISPOSAL_METHOD_CHOICES)
    retired_at = models.DateField(null=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'asset_retirements'

    def __str__(self):
        return self.disposal_method
