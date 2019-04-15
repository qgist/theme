#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

QGIST WORK BENCH
QGis 3.6 Icon Theme
https://github.com/qgist/theme

    _helper: Change icons in source code tree

    Copyright (C) 2017-2019 QGIST project <info@qgist.org>

<LICENSE_BLOCK>
The contents of this file are subject to the GNU General Public License
Version 2 ("GPL" or "License"). You may not use this file except in
compliance with the License. You may obtain a copy of the License at
https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
https://github.com/qgist/theme/blob/master/LICENSE

Software distributed under the License is distributed on an "AS IS" basis,
WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for the
specific language governing rights and limitations under the License.
</LICENSE_BLOCK>

"""


import os
import subprocess
import sys

ICON_SOURCE_FLD = 'icons'
QGIS_ROOT_FLD = '.tmp/unpacked/qgis-{VERSION:s}'
ICON_DEFAULT_FLD = 'images/themes/default'

def t(fn, target, delete = None, ch_src = None):
    return {
        'action': fn,
        'target': target,
        'delete': delete,
        'ch_src': ch_src
        }

def check_table(table_list, qgis_root_fld):

    for item in table_list:
        if item['delete'] is None and item['ch_src'] is None:
            if not os.path.isfile( os.path.join(qgis_root_fld, item['target']) ):
                print('No target: %s' % str(item))
        else:
            if not os.path.isfile( os.path.join(qgis_root_fld, item['delete']) ):
                print('No delete: %s' % str(item))
            if item['target'][:-4] != item['delete'][:-4]:
                print('Missmatch: %s' % str(item))

def get_table(version):

    source_ls = os.listdir(ICON_SOURCE_FLD)
    qgis_root_fld = QGIS_ROOT_FLD.format(VERSION = version)
    target_fld = os.path.join(qgis_root_fld, ICON_DEFAULT_FLD)
    target_ls = os.listdir(target_fld)

    names_differ = set(source_ls) - set(target_ls) - set([
        'mActionCopySelected.svg',
        'mActionShowMapTheme.svg',
        ])
    names_match = set(source_ls) & set(target_ls)

    table_list = [
        t('mActionDraw.svg', 'images/themes/default/mActionRefresh.svg'),
        t('mActionGdal.svg', 'images/themes/default/providerGdal.svg'),
        t('mActionGeoPackage.svg', 'images/themes/default/mGeoPackage.svg'),
        t('mActionOracleLayer.svg', 'images/themes/default/mActionAddOracleLayer.svg'),
        t('mActionIndicatorMemory.svg', 'images/themes/default/mIndicatorMemory.svg'),
        t('mActionIndicatorEmbedded.svg', 'images/themes/default/mIndicatorEmbedded.svg'),
        t('mActionIndicatorFilter.svg', 'images/themes/default/mIndicatorFilter.svg'),
        t('mActionDbManager.svg', 'images/themes/default/dbmanager.svg'),
        t('mActionMergeFeatAttributes.svg', 'images/themes/default/mActionMergeFeatureAttributes.svg'),
        t('mActionCadPerpendicular.svg', 'images/themes/default/cadtools/perpendicular.svg'),
        t('mActionPointSymbols.svg', 'images/themes/default/mActionOffsetPointSymbols.svg'),
        t('mActionSimplifyFeatures.svg', 'images/themes/default/mActionSimplify.svg'),
        t('mActionCadConstruction.svg', 'images/themes/default/cadtools/construction.svg'),
        t('mActionCadParallel.svg', 'images/themes/default/cadtools/parallel.svg'),
        t('mActionCad.svg', 'images/themes/default/cadtools/cad.svg'),
        t('mActionFilterMap.svg', 'images/themes/default/mActionFilter2.svg'),
        t('mActionDataDefined.svg', 'images/themes/default/mIconDataDefine.svg'),
        t('mActionAutoPlacement.svg', 'images/themes/default/mIconAutoPlacementSettings.svg'),
        t('mActionDiagramNone.svg', 'images/themes/default/diagramNone.svg'),
        t('mActionLabelBackground.svg', 'images/themes/default/propertyicons/labelbackground.svg'),
        t('mActionText.svg', 'images/themes/default/propertyicons/labeltext.svg'),
        t('mActionLabelingObstacle.svg', 'images/themes/default/labelingObstacle.svg'),
        t('mActionHistogramm.svg', 'images/themes/default/histogram.svg'),
        t('mActionLabelShadow.svg', 'images/themes/default/propertyicons/labelshadow.svg'),
        t('mActionPieChart.svg', 'images/themes/default/pie-chart.svg'),
        t('mActionLabelingNone.svg', 'images/themes/default/labelingNone.svg'),
        t('mActionRender.svg', 'images/themes/default/propertyicons/render.svg'),
        t('mActionLabelPlacement.svg', 'images/themes/default/propertyicons/labelplacement.svg'),
        t('mActionLabelBuffer.svg', 'images/themes/default/propertyicons/labelbuffer.svg'),
        t('mActionLabelFormatting.svg', 'images/themes/default/propertyicons/labelformatting.svg'),
        t('mActionPencil.svg', 'src/plugins/georeferencer/icons/default/mPushButtonPencil.svg', 'src/plugins/georeferencer/icons/default/mPushButtonPencil.png', ['mPushButtonPencil.png', 'mPushButtonPencil.svg']),
        t('mActionTracking.svg', 'images/themes/default/tracking.svg'),
        t('mActionTracking.svg', 'src/plugins/coordinate_capture/tracking.svg'),
        t('mActionLinkGeorefToQgis.svg', 'src/plugins/georeferencer/icons/default/mActionLinkGeorefToQGis.svg', 'src/plugins/georeferencer/icons/default/mActionLinkGeorefToQGis.png', ['mActionLinkGeorefToQGis.png', 'mActionLinkGeorefToQGis.svg']),
        t('mActionLinkQgisToGeoref.svg', 'src/plugins/georeferencer/icons/default/mActionLinkQGisToGeoref.svg', 'src/plugins/georeferencer/icons/default/mActionLinkQGisToGeoref.png', ['mActionLinkQGisToGeoref.png', 'mActionLinkQGisToGeoref.svg']),
        t('mActionGpsTrackBarChart.svg', 'images/themes/default/gpsicons/barchart.svg'),
        t('mActionActionRun.svg', 'images/themes/default/mAction.svg'),
        t('mActionCopyrightLabel.svg', 'images/themes/default/copyright_label.svg'),
        t('mActionDock.svg', 'images/themes/default/mDockify.svg'),
        t('mActionLegend.svg', 'images/themes/default/legend.svg'),
        t('mActionJoin.svg', 'images/themes/default/propertyicons/join.svg'),
        t('mActionGpsImporter.svg', 'src/plugins/gps_importer/gps_importer.svg'),
        t('mActionGeorefRun.svg', 'src/plugins/georeferencer/icons/default/mGeorefRun.svg', 'src/plugins/georeferencer/icons/default/mGeorefRun.png', ['mGeorefRun.png', 'mGeorefRun.svg']),
        t('mActionMetadata.svg', 'images/themes/default/propertyicons/metadata.svg'),
        t('mActionNorthArrow.svg', 'images/themes/default/north_arrow.svg'),
        t('mActionFullHistogrammStretch.svg', 'images/themes/default/mActionFullHistogramStretch.svg'),
        t('mActionCrs.svg', 'images/themes/default/propertyicons/CRS.svg'),
        t('mAction3dConfigure.svg', 'src/plugins/topology/mActionConfigure.svg'),
        t('mActionLocallCumulativeCutStretch.svg', 'images/themes/default/mActionLocalCumulativeCutStretch.svg'),
        t('mActionSignPlus.svg', 'python/plugins/processing/images/plus.svg'),
        t('mActionSignMinus.svg', 'python/plugins/processing/images/minus.svg'),
        t('mActionCoordinateCapture.svg', 'src/plugins/coordinate_capture/coordinate_capture.svg', 'src/plugins/coordinate_capture/coordinate_capture.png', ['coordinate_capture.png', 'coordinate_capture.svg']),
        t('mActionSourceFields.svg', 'images/themes/default/mSourceFields.svg'),
        t('mActionIncreaseFontSize.svg', 'images/themes/default/mActionIncreaseFont.svg'),
        t('mActionDecreaseFontSize.svg', 'images/themes/default/mActionDecreaseFont.svg'),
        t('mActionSymbology.svg', 'images/themes/default/propertyicons/symbology.svg'),
        t('mActionSettings.svg', 'images/themes/default/propertyicons/settings.svg'),
        ]

    for item in names_differ:
        itemIcon = 'mIcon' + item[7:]
        if itemIcon in target_ls:
            table_list.append(t(item, 'images/themes/default/' + itemIcon))

    for item in names_match:
        table_list.append(t(item, 'images/themes/default/' + item))

    rename = names_differ - set(item['action'] for item in table_list)
    for item in rename:
        print(item)
    assert len(rename) == 0

    check_table(table_list, qgis_root_fld)

    return table_list, qgis_root_fld

def sub(sub_from, sub_to):

    print('<< SUB from "%s" to "%s" >>' % (sub_from, sub_to))

    retval = subprocess.run(
        "find . -not -path '*/\\.*' -type f -print0 | xargs -0 sed -i 's/{X}/{Y}/g'".format(
            X = sub_from, Y = sub_to
            ),
        shell = True, check = True, stdout = subprocess.PIPE
        ).stdout.decode('utf-8')
    print(retval)

def main(version):

    table_list, qgis_root_fld = get_table(version)

    if True:
        old_cwd = os.getcwd()
        os.chdir(qgis_root_fld)
        for item in table_list:
            if item['ch_src'] is not None:
                sub(*item['ch_src'])
        os.chdir(old_cwd)

    for item in table_list:
        source_read = os.path.join(ICON_SOURCE_FLD, item['action'])
        assert os.path.isfile(source_read)
        with open(source_read, 'r', encoding = 'utf-8') as f:
            data = f.read()
        target_write = os.path.join(qgis_root_fld, item['target'])
        if item['delete'] is None:
            assert os.path.isfile(target_write)
        else:
            target_delete = os.path.join(qgis_root_fld, item['delete'])
            assert not os.path.isfile(target_write)
            assert os.path.isfile(target_delete)
            os.remove(target_delete)
        with open(target_write, 'w', encoding = 'utf-8') as f:
            f.write(data)

if __name__ == '__main__':
    main(version = sys.argv[1])
