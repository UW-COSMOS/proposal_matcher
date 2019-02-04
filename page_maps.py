import os
import shutil
import re
page_maps = [
    {'annotation': u'bbd6d3e0-4029-4563-8eaa-c06b5a2fdbb3.xml', 'prediction': u'56864edacf58f18e60df4c5e_input.pdf-0015.xml'},
    {'annotation': u'ea81856a-ba15-4d11-8857-fad1f2608c49.xml', 'prediction': u'56864edacf58f18e60df4c5e_input.pdf-0017.xml'},
    {'annotation': u'52227277-5a50-431f-b022-40022d530935.xml', 'prediction': u'56864edacf58f18e60df4c5e_input.pdf-0009.xml'},
    {'annotation': u'b994aa86-2b58-440b-9636-d9d5ec2fe7c2.xml', 'prediction': u'56864edacf58f18e60df4c5e_input.pdf-0006.xml'},
    {'annotation': u'cf8226a9-9872-4419-aec7-e25ea4a5ffa6.xml', 'prediction': u'56864edacf58f18e60df4c5e_input.pdf-0010.xml'},
    {'annotation': u'4e6338e2-c68e-4991-86e4-25c978e8c3ab.xml', 'prediction': u'56864edacf58f18e60df4c5e_input.pdf-0007.xml'},
    {'annotation': u'9da5732f-84b4-44f1-8fd5-258419827ec2.xml', 'prediction': u'56864edacf58f18e60df4c5e_input.pdf-0000.xml'},
    {'annotation': u'a934d205-3868-4e2a-a2f3-2c2df8ad6e88.xml', 'prediction': u'56864edacf58f18e60df4c5e_input.pdf-0005.xml'},
    {'annotation': u'08a2be29-0c32-4518-bd74-37b5d998f444.xml', 'prediction': u'56864edacf58f18e60df4c5e_input.pdf-0016.xml'},
        ]

def main(dir):
    for map in page_maps:
        pred_name = os.path.splitext(map["prediction"])[0]
        out = re.sub("input","gt",pred_name)
        bad_path = os.path.join(dir, out)
        good_path = os.path.join(dir, f"{out}.xml")
        shutil.move(bad_path, good_path)

if __name__ == "__main__":
    main("xml")