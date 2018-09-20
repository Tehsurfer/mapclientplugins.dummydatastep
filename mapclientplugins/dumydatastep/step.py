
"""
MAP Client Plugin Step
"""
from PySide import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.dumydatastep.configuredialog import ConfigureDialog
import json

class DumyDataStep(WorkflowStepMountPoint):
    """
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    """

    def __init__(self, location):
        super(DumyDataStep, self).__init__('DumyData', location)
        self._configured = False # A step cannot be executed until it has been configured.
        self._category = 'Testing'
        self._identifier = 'tempID'

        # Add any other initialisation code here:
        self._icon =  QtGui.QImage(':/dumydatastep/images/512px-Test_tube_icon.svg.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ecg_grid_points'))
        # Port data:
        self._portData0 = None # ecg_grid_points

        # Config:
        self._config = {}
        self._config['identifier'] = ''
        self._config['AutoDone'] = False


    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        # Put your execute step code here before calling the '_doneExecution' method.
        self._doneExecution()

    def getPortData(self, index):
        """
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.

        :param index: Index of the port to return.
        """
        ecgGrid = [[0.509204852009174, -0.5311370349544523, -0.0034167299250837833],
                   [0.5395357502061648, -0.510145753072639, -0.007247427797009046],
                   [0.5672355599089255, -0.48703701801970584, -0.012153448140377348],
                   [0.5930761300982424, -0.4624320001118838, -0.01781933727302615],
                   [0.6170586979158605, -0.4363316949788206, -0.024244589576721227],
                   [0.6392717903894952, -0.40880734759611354, -0.031393024169503986],
                   [0.6589501649806984, -0.37924310439469183, -0.03957739468908057],
                   [0.6778529320418958, -0.34905466606355257, -0.04807875500503394],
                   [0.49396373463086385, -0.5400449928328186, -0.014184277651397386],
                   [0.5219938148165804, -0.5213737210183256, -0.021750259354039705],
                   [0.5482188338281995, -0.5012497681117525, -0.03005396722860377],
                   [0.5727230851056093, -0.4797409719725964, -0.03906095065501156],
                   [0.5958093078547447, -0.45709097172323354, -0.048647480510566325],
                   [0.6171537637833796, -0.43303922855054927, -0.058945868217426825],
                   [0.6368878167933374, -0.40769146178367166, -0.06990242551847924],
                   [0.6551617261442496, -0.38116859739924286, -0.08145574164826357],
                   [0.4786410423087401, -0.5488873006489237, -0.024985164951952504],
                   [0.50436802158169, -0.5325342016632791, -0.03628736350420491],
                   [0.5285382209611089, -0.5149282339392697, -0.048225815989487504],
                   [0.551651512683225, -0.4964716857519103, -0.060596225270077624],
                   [0.5729419991860405, -0.4765481763808414, -0.07371161269096038],
                   [0.5929925504583491, -0.4556267892144881, -0.08733376004007136],
                   [0.611855196905776, -0.43374939739684715, -0.101441402557791],
                   [0.628049851147178, -0.4097248529579398, -0.1166394500463296],
                   [0.4627839639692091, -0.5572995441134712, -0.03600445512804877],
                   [0.4858847684155735, -0.5430046138234724, -0.05117491042147269],
                   [0.5087232878400857, -0.5284986012181218, -0.0664525612647761],
                   [0.5290170611193118, -0.5119446222266737, -0.08277024657295778],
                   [0.5482419145839613, -0.49453039560159, -0.09952479802961961],
                   [0.5647161909178123, -0.4749025534782857, -0.11740350680925657],
                   [0.5816541775040608, -0.4556478971093079, -0.1350926978072854],
                   [0.5975407272902518, -0.43554706312547753, -0.15321160966832706],
                   [0.4464484414499953, -0.5653267442213643, -0.0472192848228165],
                   [0.4657279848893067, -0.5521281985486189, -0.06674642703677909],
                   [0.4846600254596423, -0.5386499887545416, -0.08641559322474326],
                   [0.5023725554772778, -0.5241903385821979, -0.10658317180147975],
                   [0.5189795695333729, -0.5088409888487717, -0.12720257332472276],
                   [0.534585481775473, -0.4926859702010134, -0.14823112386714643],
                   [0.5492640292455159, -0.47578462489731665, -0.1696386871948885],
                   [0.5630515535836841, -0.4581662000426028, -0.19141041052651545],
                   [0.4268650717727057, -0.5707401347674506, -0.059761505458842935],
                   [0.4454436325574417, -0.5611491181705042, -0.08237008085827056],
                   [0.4612393379431116, -0.5493185090997809, -0.10611600566725035],
                   [0.4759003113625392, -0.5365746879476093, -0.13032569396614718],
                   [0.4895610726118554, -0.5230259138506624, -0.15494416768791758],
                   [0.5023511716655504, -0.5087764463216492, -0.17991847992520738],
                   [0.5116971489677351, -0.49175521093288904, -0.2063004002767459],
                   [0.5224816534081826, -0.47589167657065673, -0.23209439644369428],
                   [0.40867053627951044, -0.5772712343353802, -0.0717361113565054],
                   [0.42464095641280963, -0.5697529000171239, -0.09820557295299938],
                   [0.43392364037198017, -0.5568523947074416, -0.12740830369148262],
                   [0.4450283897241741, -0.5454182551824549, -0.15586635865571763],
                   [0.45511547470455493, -0.5331651174915164, -0.1847403317351347],
                   [0.46434139783432693, -0.5202189320770146, -0.21396626055132748],
                   [0.4714867061677311, -0.505598304921725, -0.2440425339491858],
                   [0.4781123574909273, -0.4905594670576076, -0.2743311904963546],
                   [0.39000920810428935, -0.5834266674645039, -0.08390149482078654],
                   [0.3989216649580346, -0.5743998774071594, -0.11605047937872888],
                   [0.4075667400902677, -0.5651579033013279, -0.14830874250112308],
                   [0.41509775595236764, -0.5550193541317798, -0.18102232020921832],
                   [0.41802707930328564, -0.541177444766751, -0.21561660370687405],
                   [0.42255639587899896, -0.528623181459634, -0.24955697203879074],
                   [0.42812246280518906, -0.5169032763742534, -0.2830736218406812],
                   [0.4258422580102747, -0.4988688315180695, -0.3197970327671987]]

        self._portData0 = ecgGrid


        return self._portData0 # ecg_grid_points

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(QtGui.QApplication.activeWindow().currentWidget())
        dlg.identifierOccursCount = self._identifierOccursCount

        if dlg.exec_():
            self._config = dlg.getConfig()
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)



        self._configured = dlg.validate()
        self._configuredObserver()
        self._configured = True

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()


