Feature: Login and get data foody

  Scenario Outline: Open foody login and scraping data
    Given Login by username and password.
    When Click into foody icon with <category>
    When Search into Ho Chi Minh with <category>
    When Handle each system store with <category>
    When Handle price each store with <category>
#    When Open google maps
#    When Save link with <category>

    Examples:
      | category   |
      | sang-trong |
#      | buffet     |
#      | nha-hang   |
#      | an-vat-via-he      |
#      | an-chay            |
#      | cafe               |
#      | quan-an            |
#      | quan-nhau          |
#      | beer-club          |
#      | tiem-banh          |
#      | tiec-tan-noi       |
#      | shop-online        |
#      | giao-com-van-phong |
#      | foodcourt          |

