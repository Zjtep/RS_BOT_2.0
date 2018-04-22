import win32api
import time
# from core import RS
from core import RSv2
import pyautogui
import cv2
from core import Screenshot
from core import Mouse
from core import Match
import numpy
from PIL import Image
import os

def transparent_test():



    # source = numpy.array(cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\1_item_slot.png"))
    source = numpy.array(cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\25_item_slot.png"))


    # NOTE The fucking thing is BLUE,GREEN, RED
    source[numpy.where((source == [41, 53, 62]).all(axis=2))] = [255, 255, 255]
    source[numpy.where((source == [44, 54, 64]).all(axis=2))] = [255, 255, 255]
    source[numpy.where((source == [38, 50, 59]).all(axis=2))] = [255, 255, 255]
    source[numpy.where((source == [45, 56, 64]).all(axis=2))] = [255, 255, 255]

    pid = "%s.png" % os.getpid()
    cv2.imwrite(pid, source)

    img = Image.open(pid)#image path and name

    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\%s"%pid, "PNG")#converted Image name
    os.remove(pid)
    print('Done')


import cv2
import numpy as np
import sys

def tran_match():


    # img = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\00_item_slot.png')
    # tmpl = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\3180.png', cv2.IMREAD_UNCHANGED)
    #
    # channels = cv2.split(tmpl)
    # mask = np.array(channels[3])
    # mask[channels[3] == 0] = 1
    # mask[channels[3] == 100] = 0

    # template_path = r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\3180.png'
    #
    # template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)
    # channels = cv2.split(template)
    # zero_channel = np.zeros_like(channels[0])
    # mask = np.array(channels[3])
    #
    # # image_path = sys.argv[2]
    # # image_path = r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\milky-way-2695569_1280.png'
    # image_path = r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\00_item_slot.png'
    # image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    #
    # mask[channels[3] == 0] = 1
    # mask[channels[3] == 100] = 0
    #
    #
    #
    #
    #
    # # mask = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\318022.png')
    # w, h = template.shape[:-1]
    # data = np.zeros((h, w, 3), dtype=np.uint8)
    #
    # transparent_mask = cv2.merge([zero_channel, zero_channel, zero_channel, mask])
    #
    # # method = ""
    # # res = cv2.matchTemplate(img, tmpl, cv2.TM_CCOEFF_NORMED, data, mask)
    # res = cv2.matchTemplate(image, template,cv2.TM_SQDIFF, data, transparent_mask)
    #
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    template_path = r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\NMk3j.png"
    template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)
    channels = cv2.split(template)
    zero_channel = np.zeros_like(channels[0])
    mask = np.array(channels[3])
    w, h = template.shape[:-1]

    image_path = r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\g6eit.png"
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    mask[channels[3] == 0] = 1
    mask[channels[3] == 100] = 0
    print cv2.__version__
    # transparent_mask = None
    # According to http://www.devsplanet.com/question/35658323, we can only use
    # cv2.TM_SQDIFF or cv2.TM_CCORR_NORMED
    # All methods can be seen here:
    # http://docs.opencv.org/2.4/doc/tutorials/imgproc/histograms/template_matching/template_matching.html#which-are-the-matching-methods-available-in-opencv
    method = cv2.TM_SQDIFF  # R(x,y) = \sum _{x',y'} (T(x',y')-I(x+x',y+y'))^2 (essentially, sum of squared differences)

    transparent_mask = cv2.merge([zero_channel, zero_channel, zero_channel, mask])
    result = cv2.matchTemplate(image, template, method, mask=transparent_mask)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print 'Lowest squared difference WITH mask', min_val
    print  min_val, max_val, min_loc, max_loc
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)

    cv2.imshow("images", np.hstack([image]))
    cv2.waitKey(0)


def tran_match2():


    # if len(sys.argv) < 3:
    #     print 'Usage: python match.py <template.png> <image.png>'
    #     sys.exit()

    # template_path = sys.argv[1]
    # template_path = r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\1496184261New-Tears-of-Joy-Emoji-Png-transparent-background.png'
    template_path = r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\8196.png'

    template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)
    channels = cv2.split(template)
    zero_channel = np.zeros_like(channels[0])
    mask = np.array(channels[3])

    # image_path = sys.argv[2]
    # image_path = r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\milky-way-2695569_1280.png'
    image_path = r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\19_item_slot.png'
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    mask[channels[3] == 0] = 1
    mask[channels[3] == 100] = 0

    # transparent_mask = None
    # According to http://www.devsplanet.com/question/35658323, we can only use
    # cv2.TM_SQDIFF or cv2.TM_CCORR_NORMED
    # All methods can be seen here:
    # http://docs.opencv.org/2.4/doc/tutorials/imgproc/histograms/template_matching/template_matching.html#which-are-the-matching-methods-available-in-opencv
    method = cv2.TM_SQDIFF  # R(x,y) = \sum _{x',y'} (T(x',y')-I(x+x',y+y'))^2 (essentially, sum of squared differences)

    transparent_mask = cv2.merge([zero_channel, zero_channel, zero_channel, mask])
    result = cv2.matchTemplate(image, template, method, mask=transparent_mask)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print 'Lowest squared difference WITH mask', min_val
    print min_val, max_val, min_loc, max_loc

    # Now we'll try it without the mask (should give a much larger error)
    transparent_mask = None
    result = cv2.matchTemplate(image, template, method, mask=transparent_mask)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print 'Lowest squared difference WITHOUT mask', min_val
    print min_val, max_val, min_loc, max_loc


def this(img_rgb, template,**kwargs):
    threshold = 0.9
    if ("threshold" in kwargs):
        threshold = kwargs['threshold']


    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # template = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\exchange_history_icon.png', 0)

    # res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_SQDIFF_NORMED)
    # threshold = 0.9
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        pt += (pt[0], pt[1])
        anchor_coord = list(pt)
        return [anchor_coord[0], anchor_coord[1], anchor_coord[2],
                anchor_coord[3]]
    return None


def trans_3():

    img = cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\00_item_slot.png")
    # template = cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\3180.png")[:, :, 2]
    template = cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\3180.png")[:, :, 2]


    cv2.imshow('Detected', template)
    cv2.waitKey(0)

    img2 = img[:, :, 2]


    # img2 = img2 - cv2.erode(img2, None)
    _,alpha = cv2.threshold(img2,0,255,cv2.THRESH_BINARY)



    cv2.imshow('Detected', alpha)
    cv2.waitKey(0)
    # # template = cv2.imread(sys.argv[2])[:, :, 2]
    # #
    # cv2.imshow('Detected', img2)
    # cv2.waitKey(0)

    # template = template - cv2.erode(template, None)

    # ccnorm = cv2.matchTemplate(img2, template, cv2.TM_CCORR_NORMED)
    ccnorm = cv2.matchTemplate(alpha, template, cv2.TM_CCORR_NORMED)
    print ccnorm.max()
    loc = numpy.where(ccnorm == ccnorm.max())
    threshold = 0.5
    th, tw = template.shape[:2]
    for pt in zip(*loc[::-1]):
        if ccnorm[pt[::-1]] < threshold:
            continue
        cv2.rectangle(img, pt, (pt[0] + tw, pt[1] + th),
                      (0, 0, 255), 2)

    cv2.imshow('Detected', img)
    cv2.waitKey(0)
    # cv2.imwrite(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\blah.png", img)


if __name__ == '__main__':
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\dry_run.png')
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\19 Apr 2018 22-56-52.png')
    # bag_icon = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\bag_icon.png', 0)
    #
    #
    #
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\00_item_slot.png')
    # bag_icon = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\10_item_slot.png', 0)
    #
    # found =  this(full_ss,bag_icon)
    # print found
    # w, h = bag_icon.shape
    # # height, width = status_buy_button.shape
    #
    # # cv2.imshow("images", np.hstack([bag_icon]))
    # # cv2.waitKey(0)
    #
    # cv2.imshow('Detected', bag_icon)
    # cv2.waitKey(0)


    trans_3()




    # cv2.rectangle(full_ss, (found[0],found[1]), (found[0]+w,found[1]+h), (0, 0, 255), 2)
    # cv2.imshow("images", np.hstack([full_ss]))
    # cv2.waitKey(0)










    # transparent_test()
    # print tran_match()

    # template_path = r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\NMk3j.png"
    # template_path = r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\4_item_slot.png"
    # template = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\4_item_slot.png', 0)
    # # template = cv2.imread(template_path,0)
    # # channels = cv2.split(template)
    # # zero_channel = np.zeros_like(channels[0])
    # # mask = np.array(channels[3])
    # # w, h = template.shape[:-1]
    #
    # image_path = r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\g6eit.png"
    # image_path = r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\19 Apr 2018 22-56-52.png"
    # image = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\dry_run.png')
    # # image = cv2.imread(image_path)
    #
    # print this(template,image)

    # window_coord = [0,0,33,37]
    #
    # window_coord[0] +=123
    # window_coord[1] += 15
    # window_coord[2] += 122
    # window_coord[3] += 14

    # inventory_ss = Screenshot.shoot(window_coord[0], window_coord[1], window_coord[2], window_coord[3],"rgb")
    # cv2.imwrite("asdfsdfsdffsd.png",inventory_ss)






    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\31 Mar 2018 21-02-10.png')
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\1 Apr 2018 02-59-46.png')
    #
    #
    # my_exchange = RSv2.GrandExchange(full_ss)
    #
    # # blah =  my_exchange.getFullCoord()
    # blah = my_exchange.getAllWindows()
    # print blah
    #
    #
    #
    # for item in blah:
    #     for key,value in item.iteritems():
    #         Screenshot.showRectangle(full_ss, value.getCoord())
    #         # print value.getStatus()
    #         print value.clickBuy()
    # # Screenshot.showRectangle(full_ss, my_inventory.getInventoryCoord())
    # cv2.imshow('Detected', full_ss)
    # cv2.imwrite("jzjz.png", full_ss)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # img = pyautogui.screenshot('ababa.png')
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\ababa.png')
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\inventory_sample.png')
    # robes = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\3_item_slot (3).png')
    # my_inventory = RSv2.Inventory(full_ss)

    # print my_inventory.findItem(full_ss,robes)
    # print my_inventory.getAllItems()





    # my_inventory.screenShotInventory(full_ss)


    # my_inventory.screenShotInventory(full_ss)

    # for item in item_position:


    # for item in my_inventory.getInventory([23,27]):
    #     for key,value in item.iteritems():
    #         Screenshot.showRectangle(full_ss, value)
    # # Screenshot.showRectangle(full_ss, my_inventory.getInventoryCoord())
    # cv2.imshow('Detected', full_ss)
    # cv2.imwrite("jzjz.png", full_ss)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



    # Screenshot.showRectangle(full_ss, item_position)
    # cv2.imshow('Detected', full_ss)
    # cv2.imwrite("jzjz.png", full_ss)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # for index, item in enumerate(my_inventory.getFullInventory()):
    #     # if index >= 2 and index<=5:
    #     if index >= 15 and index <= 24:
    #         for key,value in item.iteritems():
    #             Screenshot.showRectangle(full_ss, value)
    # cv2.imshow('Detected', full_ss)
    # cv2.imwrite("jzjz.png", full_ss)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()