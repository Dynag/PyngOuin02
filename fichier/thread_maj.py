import threading
import traceback
import fichier.lib.urllib3 as urllib3
import fichier.lib.xmltodict as xmltodict
import fichier.var as var
import fichier.design as design
import webbrowser
import os


def getxml():
    try:
        url = var.site + "/PyngOuin/changelog.xml"
        http = urllib3.PoolManager(cert_reqs='CERT_NONE')
        response = http.request('GET', url)

        data = xmltodict.parse(response.data)
        return data
    except:
        print("Failed to parse xml from response (%s)" % traceback.format_exc())
        pass


def recupDerVer():
    try:
        xml = getxml()
        i = 0;
        for val in xml["changelog"]["version"]:
            if i == 0:
                verion2 = val["versio"]
                i += 1
        version1 = verion2.split(".")
        version = version1[0] + version1[1] + version1[2]
        return version
    except:
        pass


def testVersion():
    version = recupDerVer()
    versionlog = var.version.split(".")
    versionlog1 = versionlog[0] + versionlog[1] + versionlog[2]
    if int(versionlog1) < int(version):
        val = design.question_box('Mise à jour', 'Une mise à jour vers la version ' + str(
            version) + ' est disponible. \n Voulez vous la télécharger ?')
        print(val)
        if val == True:
            webbrowser.open(var.site + '/PyngOuin/PyngOuin%20Setup.exe')
            os.exit(0)
    else:
        pass


def main():
    try:
        testVersion()
    except:
        pass
    #threading.currentThread().join()
