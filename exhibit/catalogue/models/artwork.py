from django.db import models
from django.utils.translation import ugettext as _
from django.urls import reverse

from datetime import date
from operator import itemgetter

from catalogue.models.activity import SaleData

class ArtworkImage(models.Model):
    """A model representing an image file"""

    image = models.ImageField(
        'Image',
        upload_to="artworks/",
        help_text="Sample image of the artwork"
    )    
    artwork = models.ForeignKey('Artwork', on_delete=models.CASCADE, null=True, blank=True)

class Artwork(models.Model):
    """A model representing an individual work of art"""

    # optional_field = {'blank' : True, 'null' : true}


    ## Mandatory Fields ##
    image = models.ImageField(
        'Image',
        upload_to="artworks/",
        null=True,
        help_text="Sample image of the artwork",
        blank = True
    )
    title = models.CharField('Title', max_length=200, help_text="Artwork title")
    series = models.ForeignKey('Series', on_delete=models.SET_NULL, null=True)
    year = models.IntegerField('Year', help_text='Year of creation')

    # Optional Fields ##
    width_cm = models.FloatField("Width cm",
                                 default=0.0,
                                 help_text="W",
                                 null=True,
                                 blank=True,
                                 )
    height_cm = models.FloatField("Height cm",
                                  default=0.0,
                                  help_text="H",
                                  null=True,
                                  blank=True,
                                  )
    depth_cm = models.FloatField("Depth cm",
                                 default=0.0,
                                 help_text="D",
                                 null=True,
                                 blank=True,
                                 )
    width_in = models.FloatField("Width in",
                                 default=0.0,
                                 help_text="W",
                                 null=True,
                                 blank=True,
                                 )
    height_in = models.FloatField("Height in",
                                  default=0.0,
                                  help_text="H",
                                  null=True,
                                  blank=True,
                                  )
    depth_in = models.FloatField("Depth in",
                                 default=0.0,
                                 help_text="D",
                                 null=True,
                                 blank=True,
                                 )

    SIZE_OPTIONS = (
        ('1', 'Small'),
        ('2', 'Medium'),
        ('3', 'Large'),
        ('4', 'Extra Large'),
        ('9', 'Scroll'),
    )

    size = models.CharField('Size Category',
                            max_length=1,
                            choices=sorted(SIZE_OPTIONS, key=itemgetter(0)),
                            blank=True,
                            help_text="Size"
                            )
    medium = models.CharField('Medium', max_length=250, blank=True,
                              default='Diluted acrylic on canvas', help_text="medium of creation")

    # Mutable Fields - are expected to change over time ##

    location = models.ForeignKey('Location',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 help_text="Current location"
                                 )

    ROLL_STATUS_CHOICES = (
        ('R', 'Rolled'),
        ('S', 'Stretched'),
    )

    rolled = models.CharField('Rolled/Streched', max_length=1, choices=ROLL_STATUS_CHOICES,
                              blank=True)

    framed = models.BooleanField('Framed', blank=True, default=False)

    OVERALL_STATUS_CHOICES = (
        ('D', 'Draft'),
        ('A', 'Avaliable'),
        ('B', 'Dibs'),
        ('O', 'On Loan'),
        ('S', 'Sold'),
    )
    status = models.CharField('Status', max_length=1, choices=OVERALL_STATUS_CHOICES,
                              default='D', blank=True, help_text="Current status")
    additional = models.TextField('Additional info', blank=True, help_text="Anything else of interest")

    # Sale fields
    owner = models.CharField('Owner', max_length=200, default='Rotem Reshef', help_text="Current owner", blank=True)
    sold_by = models.CharField('Sold By', max_length=200, blank=True, help_text="The agent's name")
    price_nis = models.DecimalField("Price in NIS",
                                    max_digits=10,
                                    decimal_places=2,
                                    null=True,
                                    blank=True,
                                    help_text="Price NIS"
                                    )
    price_usd = models.DecimalField("Price in US Dollars",
                                    max_digits=10,
                                    decimal_places=2,
                                    null=True,
                                    blank=True,
                                    help_text="Price USD"
                                    )
    sale_price = models.DecimalField("Sale Price",
                                     max_digits=10,
                                     decimal_places=2,
                                     null=True,
                                     blank=True,
                                     help_text="Price of final sale"
                                     )
    sale_currency = models.CharField("Sale currency", max_length=10, blank=True)
    discount = models.DecimalField("Discount",
                                   max_digits=10,
                                   decimal_places=2,
                                   null=True,
                                   blank=True,
                                   help_text="Discount if any"
                                   )
    sale_date = models.DateField("Sale Date", blank=True, null=True)

    # @TODO convert owner to foreignkey

    def __str__(self):
        """string representation of model"""
        return self.title

    def get_absolute_url(self):
        return reverse('catalogue:artwork_detail', kwargs={'pk': self.pk})

    @property
    def get_image(self):
        """newest image associated with artwork"""
        image_model_instance = ArtworkImage.objects.filter(artwork=self.pk).last()
        if not image_model_instance:
            image_model_instance = ArtworkImage()

        result = image_model_instance.image
        result.pk = image_model_instance.pk
        return result

    @property
    def sale_data(self):
        """newest image associated with artwork"""
        sale_data_instance = SaleData.objects.filter(artwork=self.pk).last()
        return sale_data_instance

    searchable_fields = [
        series,
        title,
        location,
        status,
        year,
        size,
        medium,
        rolled,
        owner,
    ]

class Series(models.Model):
    """A model representing a series of artworks"""

    name = models.CharField("Name", max_length=200, help_text="Series name")
    description = models.TextField("Description", blank=True)

    def __str__(self):
        """string representation of model"""
        return self.name

    def get_absolute_url(self):
        return reverse('catalogue:series_detail', kwargs={'pk': self.pk})

    searchable_fields = [
        name,
    ]

    @property
    def count(self):
        """number of artworks in series"""

        return Artwork.objects.filter(series__pk=self.pk).count()

    @property
    def time_range(self):
        """range of years for works in Series. returns None if empty"""
        if self.count == 0:
            return None

        artworks_in_series = Artwork.objects.filter(series__pk=self.pk).order_by('year')
        return {'first': artworks_in_series.first().year, 'last': artworks_in_series.last().year}

    @property
    def image(self):
        """image field for newest artwork in Series"""
        if self.count == 0:
            return None

        artworks_in_series = Artwork.objects.filter(series__pk=self.pk).order_by('-pk')
        return artworks_in_series.first().get_image