from django.contrib import admin
from .models import VendorCategory, Vendor, EventPackage, Booking, ContactInfo

admin.site.site_header = "Opal Movement Planners - Admin Panel"
admin.site.site_title = "Opal Admin"
admin.site.index_title = "Welcome to Opal Movement Planners Admin Panel"

class VendorInline(admin.TabularInline):
    model = Vendor
    extra = 1
    fields = ('name', 'experience', 'phone', 'photo', 'is_active')
    show_change_link = True

@admin.register(VendorCategory)
class VendorCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    inlines = [VendorInline]

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'experience', 'phone', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'description']
    list_select_related = ['category']

@admin.register(EventPackage)
class EventPackageAdmin(admin.ModelAdmin):
    list_display = ['event_type', 'with_catering_price', 'decor_only_price', 'persons', 'package_image']
    list_filter = ['event_type', 'is_active']
    fieldsets = (
        ('Event Details', {
            'fields': ('event_type', 'name', 'persons', 'description')
        }),
        ('Pricing', {
            'fields': ('with_catering_price', 'decor_only_price')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

    def package_image(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" style="border-radius: 5px;" />'
        return 'No Image'
    package_image.short_description = 'Package Image'
    package_image.allow_tags = True

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'phone', 'event_type', 'package_name', 'event_date', 'guest_count', 'status', 'created_at']
    list_filter = ['status', 'event_type', 'event_date', 'created_at']
    search_fields = ['customer_name', 'phone', 'email']
    list_editable = ['status']
    readonly_fields = ['created_at']
    ordering = ['-created_at']

    fieldsets = (
        ('Customer Information', {
            'fields': ('customer_name', 'phone', 'email')
        }),
        ('Event Details', {
            'fields': ('event_type', 'package', 'event_date', 'guest_count', 'special_requests')
        }),
        ('Booking Status', {
            'fields': ('status', 'created_at')
        }),
    )

    def package_name(self, obj):
        return obj.package.name if obj.package else 'Custom Package'
    package_name.short_description = 'Package'
    package_name.admin_order_field = 'package__name'

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['owner_name', 'phone', 'is_primary']
