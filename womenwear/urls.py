from imaplib import _Authenticator
import profile
from re import template
from tokenize import Name
from xml.etree.ElementInclude import include
from django.core.mail import EmailMessage
from django.urls import path
from django.contrib.auth import views as auth_views
from womenwear import views
from .forms import (
    LoginForm,
    MyPasswordChangeForm,
    MypasswordResetForm,
    MySetPasswordForm,
)

urlpatterns = [
    path("", views.home, name="homeind"),
    path("womens_kurta/", views.womens_kurta, name="kurtaind"),
    path("women/", views.women, name="womenind"),
    path("womenPalazzo&pants/", views.WomenPalazzo_pants, name="womenPalazzo&pantsind"),
    path("womenLehenga/", views.WomenLehenga, name="womenLehengaind"),
    path("womenSkirts/", views.WomenSkirts, name="womenSkirtsind"),
    path("womenNight_Wear/", views.WomenNight_Wear, name="womenNight_Wearind"),
    path("womenCasual_Wear/", views.WomenCasual_Wear, name="womenCasual_Wearind"),
    path("womenParty_Wear/", views.WomenParty_Wear, name="womenParty_Wearind"),
    path("womenBlouse/", views.WomenBlouse, name="womenBlouseind"),
    path("husband/", views.husband, name="husbandind"),
    path("husbandShirts/", views.HusbandShirts, name="husbandShirtsind"),
    path(
        "husbandEmbroideredkurta/",
        views.HusbandEmbroideredkurta,
        name="husbandEmbroideredkurtaind",
    ),
    path("husbandWaistcoat/", views.HusbandWaistcoat, name="husbandWaistcoatind"),
    path("husbandKurta/", views.HusbandKurta, name="husbandKurtaind"),
    path("husbandShortkurta/", views.HusbandShortkurta, name="husbandShortkurtaind"),
    path(
        "husbandKurtapajamaset/",
        views.HusbandKurtapajamaset,
        name="husbandKurtapajamasetind",
    ),
    path("husbandSherwani/", views.HusbandSherwani, name="husbandSherwaniind"),
    path("husbandNightWear/", views.HusbandNightWear, name="husbandNightWearind"),
    path("accessories/", views.accessories, name="accessoriesind"),
    path("international/", views.international, name="itorderind"),
    path("Kids_Wear/", views.Kids_Wear, name="Kids_Wearind"),
    path("kidsgirlsFrocks/", views.KidsgirlsFrocks, name="kidsgirlsFrocksind"),
    path("kidsgirlsKurtasets/", views.KidsgirlsKurtasets, name="kidsgirlsKurtasetsind"),
    path(
        "kidsgirlsLehengasets/",
        views.kidsgirlsLehengasets,
        name="kidsgirlsLehengasetsind",
    ),
    path(
        "kidsgirlsTops_Tunics/",
        views.kidsgirlsTops_Tunics,
        name="kidsgirlsTops_Tunicsind",
    ),
    path(
        "kidsgirlsNight_Wear/", views.kidsgirlsNight_Wear, name="kidsgirlsNight_Wearind"
    ),
    path("kidsboysKurta/", views.kidsboysKurta, name="kidsboysKurtaind"),
    path("kidsboysKurtasets/", views.kidsboysKurtasets, name="kidsboysKurtasetsind"),
    path("kidsboysPartyWear/", views.kidsboysPartyWear, name="kidsboysPartyWearind"),
    path("kidsboysShirt/", views.kidsboysShirt, name="kidsboysShirtind"),
    path("kidsboysNightWear/", views.kidsboysNightWear, name="kidsboysNightWearind"),
    path("jewellery/", views.jewellery, name="jewelleryind"),
    path("Fashion_jewellery/", views.Fashion_jewellery, name="Fashion_jewelleryind"),
    path("Earrings/", views.Earrings, name="Earringsind"),
    path("Flower_jewellery/", views.Flower_jewellery, name="Flower_jewelleryind"),
    path("Silver_jewellery/", views.Silver_jewellery, name="Silver_jewelleryind"),
    path("Necklace_Pendant/", views.Necklace_Pendant, name="Necklace_Pendantind"),
    path("Bracelets_Bangle/", views.Bracelets_Bangle, name="Bracelets_Bangleind"),
    path("Rings/", views.Ringsjewellery, name="Ringsind"),
    path("Hair_Accessories/", views.Hair_Accessories, name="Hair_Accessoriesind"),
    path("Scarf/", views.Scarf, name="Scarfind"),
    path("Menjewellery/", views.Menjewellery, name="Menjewelleryind"),
    path("Kids_jewellery/", views.Kids_jewellery, name="Kids_jewelleryind"),
    path("Suit_Kurta/", views.womens_suit, name="suitind"),
    path("waistband/", views.waistband, name="waistbandind"),
    path("Potli/", views.Potli, name="Potliind"),
    path("Personal_care/", views.Personal_care, name="Personal_careind"),
    path("Wedding_Collection/", views.Wedding_Collection, name="Wedding_Collectionind"),
    path("Groom/", views.Groom, name="Groomind"),
    path("womens_top/", views.womens_top, name="topind"),
    path("womens_goun/", views.womens_goun, name="gounind"),
    path("Bride/", views.Bride, name="Brideind"),
    path("Groom_Bride_Family/", views.Groom_Bride_Family, name="Groom_Bride_Familyind"),
    path("Bridesmaids/", views.Bridesmaids, name="Bridesmaidsind"),
    path(
        "Designer_Collection/", views.Designer_Collection, name="Designer_Collectionind"
    ),
    path("Under_799/", views.Under_799, name="Under_799ind"),
    path("Under_899/", views.Under_899, name="Under_899ind"),
    path("Under_999/", views.Under_999, name="Under_999ind"),
    path("womens_indo/", views.womens_indo, name="indoind"),
    path("product/<slug>", views.product, name="detailsind"),
    path("about-us/", views.about, name="aboutind"),
    path("contact-us/", views.Contact, name="contactind"),
    path("wishlist/", views.Wishlist, name="wishlistind"),
    path("listview/", views.list, name="listind"),
    path("remove_list/", views.remove_list, name="remove_listind"),
    path("policy/", views.policy, name="policyind"),
    path("support/", views.support, name="supportind"),
    path("Wholesale/", views.Wholesale, name="Wholesaleind"),
    path("terms/", views.terms, name="termsind"),
    path("size/", views.size, name="sizeind"),
    path("shipping/", views.shipping, name="shippingind"),
    path("exchange/", views.exchange, name="exchangeind"),
    path("payment/", views.payment, name="paymentind"),
    path("search/", views.search, name="searchind"),
    path("signup/", views.CustomerRegistrationView.as_view(), name="loginind"),
    path("add-to-cart/", views.cart, name="add-to-cartind"),
    path("add-to-wishlist/", views.removelist, name="add-to-wishlistind"),
    path("checkout/", views.checkout, name="checkoutind"),
    path("order/", views.order, name="orderind"),
    path("paymentdone/", views.payment_done, name="paymentdoneind"),
    path("cart/", views.show_cart, name="showcartind"),
    path("pluscart/", views.plus_cart),
    path("minuscart/", views.minus_cart),
    path("Removecart/", views.remove_cart),
    path("removewishlist/", views.remove_wishlist),
    path(
        "signin/",
        auth_views.LoginView.as_view(
            next_page="homeind",
            template_name="../templates/india/signin.html",
            authentication_form=LoginForm,
        ),
        name="signinind",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="signinind"),
        name="logoutind",
    ),
    path("profile/", views.ProfileView.as_view(), name="profileind"),
    path(
        "changepassword/",
        auth_views.PasswordChangeView.as_view(
            template_name="../templates/india/changepassword.html",
            form_class=MyPasswordChangeForm,
            success_url="/passwordchangedone/",
        ),
        name="changepasswordind",
    ),
    path(
        "passwordchangedone/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="../templates/india/passwordchangedone.html"
        ),
        name="passwordchangedoneind",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="../templates/india/password_reset.html",
            form_class=MypasswordResetForm,
        ),
        name="password_resetind",
    ),
    path(
        "password-reset-done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="../templates/india/password_reset_done.html"
        ),
        name="password_reset_doneind",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="../templates/india/password_reset_confirm.html",
            form_class=MySetPasswordForm,
        ),
        name="password_reset_confirmind",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="../templates/india/password_reset_complete.html"
        ),
        name="password_reset_completeind",
    ),
    path("address/", views.address, name="addressind"),
    path("removeadd/", views.remove_add),
    path("invoice/", views.invoice, name="invoiceind"),
    path("pdf/", views.render_pdf_view, name="render_pdf_viewind"),
]
