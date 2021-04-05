from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.translation import gettext_lazy as _

from circularis.base.models import Address
from circularis.accounts.models import User


class BookCategoryManager(models.Manager):

    def populate(self, recreate=False):
        book_category = [
            ('NCL', '-----------------------'),
            ('ANT', 'ANTIQUES & COLLECTIBLES'),
            ('ARC', 'ARCHITECTURE'),
            ('ART', 'ART'),
            ('BIB', 'BIBLES'),
            ('BIO', 'BIOGRAPHY & AUTOBIOGRAPHY'),
            ('BOD', 'BODY, MIND & SPIRIT'),
            ('BUS', 'BUSINESS & ECONOMICS'),
            ('COM', 'COMICS & GRAPHIC NOVELS'),
            ('CMP', 'COMPUTERS'),
            ('COO', 'COOKING'),
            ('CRA', 'CRAFTS & HOBBIES'),
            ('DES', 'DESIGN'),
            ('DRA', 'DRAMA'),
            ('EDU', 'EDUCATION'),
            ('FAM', 'FAMILY & RELATIONSHIPS'),
            ('FIC', 'FICTION'),
            ('FOR', 'FOREIGN LANGUAGE STUDY'),
            ('GAM', 'GAMES & ACTIVITIES'),
            ('GAR', 'GARDENING'),
            ('HEA', 'HEALTH & FITNESS'),
            ('HIS', 'HISTORY'),
            ('HOU', 'HOUSE & HOME'),
            ('HUM', 'HUMOR'),
            ('JUV', 'JUVENILE FICTION'),
            ('JUN', 'JUVENILE NONFICTION'),
            ('LAN', 'LANGUAGE ARTS & DISCIPLINES'),
            ('LAW', 'LAW'),
            ('LIT', 'LITERARY COLLECTIONS'),
            ('LIC', 'LITERARY CRITICISM'),
            ('MAT', 'MATHEMATICS'),
            ('MED', 'MEDICAL'),
            ('MUS', 'MUSIC'),
            ('NAT', 'NATURE'),
            ('PER', 'PERFORMING ARTS'),
            ('PET', 'PETS'),
            ('PHI', 'PHILOSOPHY'),
            ('PHO', 'PHOTOGRAPHY'),
            ('POE', 'POETRY'),
            ('POL', 'POLITICAL SCIENCE'),
            ('PSY', 'PSYCHOLOGY'),
            ('REF', 'REFERENCE'),
            ('REL', 'RELIGION'),
            ('SCI', 'SCIENCE'),
            ('SEL', 'SELF-HELP'),
            ('SOC', 'SOCIAL SCIENCE'),
            ('SPO', 'SPORTS & RECREATION'),
            ('STU', 'STUDY AIDS'),
            ('TEC', 'TECHNOLOGY & ENGINEERING'),
            ('TRA', 'TRANSPORTATION'),
            ('TRV', 'TRAVEL'),
            ('TRU', 'TRUE CRIME'),
            ('YOU', 'YOUNG ADULT FICTION'),
            ('YOA', 'YOUNG ADULT NONFICTION)]')]

        if recreate:
            print("deleting data")
            self.delete()
        else:
            if self.all():
                print(f"There is data in {self.model.__name__}. Nothing to do.")
                return False

        for b_category in book_category:
            code, status = b_category
            self.create(code=code, status=status)
            print(f"Populating {self.model.__name__} model with: {code}, {status}")

        return True


class BookCategory(models.Model):
    class BookCategoryChoices(models.TextChoices):
        NCL = 'NCL', _('-----------------------')
        ANT = 'ANT', _('ANTIQUES & COLLECTIBLES')
        ARC = 'ARC', _('ARCHITECTURE')
        ART = 'ART', _('ART')
        BIB = 'BIB', _('BIBLES')
        BIO = 'BIO', _('BIOGRAPHY & AUTOBIOGRAPHY')
        BOD = 'BOD', _('BODY, MIND & SPIRIT')
        BUS = 'BUS', _('BUSINESS & ECONOMICS')
        COM = 'COM', _('COMICS & GRAPHIC NOVELS')
        CMP = 'CMP', _('COMPUTERS')
        COO = 'COO', _('COOKING')
        CRA = 'CRA', _('CRAFTS & HOBBIES')
        DES = 'DES', _('DESIGN')
        DRA = 'DRA', _('DRAMA')
        EDU = 'EDU', _('EDUCATION')
        FAM = 'FAM', _('FAMILY & RELATIONSHIPS')
        FIC = 'FIC', _('FICTION')
        FOR = 'FOR', _('FOREIGN LANGUAGE STUDY')
        GAM = 'GAM', _('GAMES & ACTIVITIES')
        GAR = 'GAR', _('GARDENING')
        HEA = 'HEA', _('HEALTH & FITNESS')
        HIS = 'HIS', _('HISTORY')
        HOU = 'HOU', _('HOUSE & HOME')
        HUM = 'HUM', _('HUMOR')
        JUV = 'JUV', _('JUVENILE FICTION')
        JUN = 'JUN', _('JUVENILE NONFICTION')
        LAN = 'LAN', _('LANGUAGE ARTS & DISCIPLINES')
        LAW = 'LAW', _('LAW')
        LIT = 'LIT', _('LITERARY COLLECTIONS')
        LIC = 'LIC', _('LITERARY CRITICISM')
        MAT = 'MAT', _('MATHEMATICS')
        MED = 'MED', _('MEDICAL')
        MUS = 'MUS', _('MUSIC')
        NAT = 'NAT', _('NATURE')
        PER = 'PER', _('PERFORMING ARTS')
        PET = 'PET', _('PETS')
        PHI = 'PHI', _('PHILOSOPHY')
        PHO = 'PHO', _('PHOTOGRAPHY')
        POE = 'POE', _('POETRY')
        POL = 'POL', _('POLITICAL SCIENCE')
        PSY = 'PSY', _('PSYCHOLOGY')
        REF = 'REF', _('REFERENCE')
        REL = 'REL', _('RELIGION')
        SCI = 'SCI', _('SCIENCE')
        SEL = 'SEL', _('SELF-HELP')
        SOC = 'SOC', _('SOCIAL SCIENCE')
        SPO = 'SPO', _('SPORTS & RECREATION')
        STU = 'STU', _('STUDY AIDS')
        TEC = 'TEC', _('TECHNOLOGY & ENGINEERING')
        TRA = 'TRA', _('TRANSPORTATION')
        TRV = 'TRV', _('TRAVEL')
        TRU = 'TRU', _('TRUE CRIME')
        YOU = 'YOU', _('YOUNG ADULT FICTION')
        YOA = 'YOA', _('YOUNG ADULT NONFICTION')

    code = models.CharField(max_length=3, unique=True, choices=BookCategoryChoices.choices,
                            default=BookCategoryChoices.NCL)
    status = models.CharField(max_length=30)

    objects = BookCategoryManager()

    def __str__(self):
        return self.status

    class Meta:
        ordering = ['status']
        verbose_name_plural = 'categories'


class BookStatusManager(models.Manager):

    def populate(self, recreate=False):
        book_status = [('AV', 'Available'),
                       ('CO', 'Checked out'),
                       ('UN', 'Unavailable'),
                       ('RM', 'Removed')]

        if recreate:
            print("deleting data")
            self.delete()
        else:
            if self.all():
                print(f"There is data in {self.model.__name__}. Nothing to do.")
                return False

        for b_status in book_status:
            code, status = b_status
            self.create(code=code, status=status)
            print(f"Populating {self.model.__name__} model with: {code}, {status}")

        return True


class BookStatus(models.Model):
    class BookStatusChoices(models.TextChoices):
        AV = 'AV', _('Available')
        RE = 'RE', _('I am reading')
        LO = 'LO', _('Locked')
        RM = 'RM', _('Removed')

    code = models.CharField(max_length=2, unique=True, choices=BookStatusChoices.choices, default=BookStatusChoices.AV)
    status = models.CharField(max_length=25)

    objects = BookStatusManager()

    def __str__(self):
        return self.status

    class Meta:
        ordering = ['status']
        verbose_name_plural = 'bookstatus'


class BookManager(models.Manager):

    def get_books(self):
        try:
            return self.filter()
        except ObjectDoesNotExist:
            return []

    def get_books_by_user(self, user):
        try:
            return self.filter(user=user.id)
        except ObjectDoesNotExist:
            return []

    def get_books_by_status_code(self, code='AV'):
        try:
            return self.get(status=code)
        except ObjectDoesNotExist:
            return []

    def get_book_by_genre(self, category='NCL'):
        try:
            return self.get(category=category)
        except ObjectDoesNotExist:
            return []


class Book(models.Model):
    title = models.CharField(max_length=60, blank=False)
    # subtitle = models.CharField(max_length=60, blank=True, null=True)
    #
    author_1 = models.CharField(max_length=60, blank=False)
    # author_2 = models.CharField(max_length=60, blank=True, null=True)
    # author_3 = models.CharField(max_length=60, blank=True, null=True)
    #
    # publisher = models.CharField(max_length=60, blank=True, null=True)
    # publishedDate = models.CharField(max_length=4, blank=True, null=True)
    #
    # description = models.CharField(max_length=256, blank=True, null=True)
    #
    # isbn_10 = models.CharField(max_length=10, blank=True, null=True)
    # isbn_13 = models.CharField(max_length=13, blank=True, null=True)
    #
    # pages = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(BookCategory, blank=False, on_delete=models.DO_NOTHING)
    #
    thumbnail = models.BinaryField(blank=True)
    #
    address = models.ForeignKey(Address, blank=False, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(BookStatus, to_field='code', blank=False, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, blank=False, on_delete=models.DO_NOTHING)
    #
    objects = BookManager()

    def __str__(self):
        return self.title

    def to_str(self):
        return f"{self.title}"

    class Meta:
        ordering = ['title']
