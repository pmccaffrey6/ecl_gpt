Basics
High performance liquid chromatography (HPLC) separates sample mixtures into analyzable molecular constituents by injection into flowing liquid that passes through a retentive column:
input textExperimentLCMS[mySamples]https://wolfram.com/xid/01wdxue0nyhermi-b3z140
MassAnalyzer
Use MassAnalyzer option to select TripleQuadruploe as the mass analyzer
input textExperimentLCMS[mySamples,
 	MassAnalyzer -> TripleQuadruploe,
 	ConeGasFlow -> (90 * PSI)
 ]https://wolfram.com/xid/01wdxue0nyhermi-85acf
Separation Mode and Gradient



This documentation describes the ExperimentLCMS function that is part of the Symbolic Lab Language (SLL) package written in Wolfram Language.

ExperimentLCMS
ExperimentLCMS[Samples]⟹Protocol
generates a Protocol to separate and analyze Samples via Liquid Chromatography Mass Spectrometry (LCMS).

    
Liquid chromatography - Mass Spectrometry (LC-MS) separates samples injected into a liquid flow by passage through an adsorbent column (see ExperimentHPLC). After separation, analytes are ionized, selected, and detected in the Mass Spectrometer device (see ExperimentMassSpectrometry). Within, ions are resolved by their mass versus charge state. Optionally, ions can be fragmented by collision with an inert gas, and the resulting product ions can, in turn, be resolved and detected for more information. In total, LC-MS can answer composition questions; for example, proteins, lipids, and metabolites can be identified in a sample. Furthermore, LC-MS can answer concentration questions; for instance, nucleotides can be quantified in a biological sample.
   

Experimental Principles
=======================

Step 1: The system is rinsed with cleaning solutions. Step 2: The stationary column is installed and equilibrated to measurement conditions. Step 3: Samples are then introduced into the flow path. Step 4: The analytes are selectively retained on the downstream column. Step 5: Upon exit from the column, the now separated analytes are analyzed according to their physical property using a mass spectrometer. Step 6: After final sample measurement, the Column(s) are rinsed, removed from the system, and stowed. Step 7: After the column is removed, the system is rinsed with cleaning solution.

Instrumentation
===============

### Waters Acquity UPLC I-Class PDA

Buffer solutions (up to 4) are steadily pumped through the instrument, consisting of a 6-port valve system, adsorbent column, detectors, and terminates at fraction collection or waste. Samples within the autosampler are loaded into the sample loop via positive displacement from the syringe. The rotation of the valve exposes the sample loop, thereby carrying the sample downstream to the column. Within the column, molecular constituents are separated by adsorption -- a function of the buffers, column, sample properties and temperature. Analytes are continuously carried downstream to the detectors, where they can elicit quantifiable peak signals.

Principle of PhotodiodeArray detection. Filtered light (across a range of wavelengths) passes through the flow downstream of the column. Presence of light-absorbing molecules will result in less light transmission to the recipient Diode, thereby producing a chromatographic peak for each specific wavelength.

### Xevo G2-XS QTOF

The samples to be lyophilized are placed into the lyophilizer’s central chamber, resting on the sample shelves which control the sample and chamber temperature. Below the sample shelf is a coiled condenser, which operates around -85°C during lyophilization. This condenser re-freezes any solvent that has sublimated away from the samples in the chamber, forming a dense layer of frozen solvent. A vacuum pump is attached to the instrument, and is capable of dropping the chamber pressure to 100mTorr. Chamber atmosphere, along with any solvent with freezing temperatures below the condenser temperature, escapes through the vacuum pump into the building’s ventilation system. A waste line connects the condenser to a waste container, and will allow for the disposal of the thawed solvent after the lyophilization run.

### QTRAP 6500

Principles of an electrospray triple quadrupole mass spectrometer (ESI-QQQ). Analytes are injected through the capillary tube into the source block at the desired InfusionFlowRate. Once the sample enters the source block, it is evaporated at the DesolvationTemperature under a stream of nitrogen gas with a pressure of DesolvationGasFlow. ESICapillaryVoltage is then applied to the capillary tubing tip to produce an electrospray, which turns into single gas-phase ions due to additional evaporation and desolvation SourceTemperature. Ions, focused by the ConeGasFlow, enter the mass spectrometer through the source cone and follow the ion path via an applied voltage (DeclusteringVoltage). They are then guided through an ion guide path via another applied voltage (IonGuideVoltange) to generate a focused ion beam. Ions travel through the first quadrupole mass analyzer (MS1), where their mass is resolved by their mass-to-charge ratio (m/z, MassDetection). After the MS1, ions enter the collision cell, where they can be fragmented by collision-induced dissociation, resulting in bond breakage and the fragmentation of the molecular ions into smaller fragments. CollisionCellExitVoltage accelerates and guides the fragmented ions to enter the second quadrupole mass analyzer (MS2), where their mass can be resolved again by their m/z (FragmentMassDetection). Spectra are continuously acquired for ions either inside MassDetection as a ranged value or as a fixed value, hitting the detector during ScanTime until the end of RunDuration, and a total mass spectrum is generated.

Experiment Options
==================

General

SeparationMode

    - The category of method used to elicit differential column retention. This option is used to resolve the column, buffers, temperature, and pressure limits.

    - Default Value: ReversePhase

    - Pattern Description: NormalPhase, ReversePhase, IonExchange, SizeExclusion, Affinity, or Chiral.

    - Programmatic Pattern: SeparationModeP


MassAnalyzer

    - The manner of detection used to resolve and detect molecules. QTOF accelerates ions through an elongated flight tube and separates ions by their flight time (related to mass to charge ratio).

    - Default Value: Automatic

    - Default Calculation: Is automatically set to the QTOF.

    - Pattern Description: QTOF or TripleQuadrupole.

    - Programmatic Pattern: (QTOF | TripleQuadrupole) | Automatic

ChromatographyInstrument

    - The device used to separate molecules from the sample mixture using mobile liquid through an adsorbent column.

    - Default Value: Model\[Instrument, HPLC, Waters Acquity UPLC I-Class PDA\]

    - Default Calculation: Automatically set to an instrument model that is available for the best MassSpectrometerInstrument.

    - Pattern Description: An object of type or subtype Model\[Instrument, HPLC\] or Object\[Instrument, HPLC\]

    - Programmatic Pattern: ObjectP\[{Model\[Instrument, HPLC\], Object\[Instrument, HPLC\]}\]


MassSpectrometerInstrument

    - The device used to ionize, separate, fragment (optionally), and detect analyte species.

    - Default Value: Automatic

    - Default Calculation: Is automatically set according to MassAnalyzer: Model\[Instrument, MassSpectrometer, "Xevo G2-XS QTOF"\] for QTOF, Model\[Instrument, MassSpectrometer, "QTRAP 6500"\] for using TripleQuadrupole.

    - Pattern Description: An object of type or subtype Model\[Instrument, MassSpectrometer\] or Object\[Instrument, MassSpectrometer\]

    - Programmatic Pattern: ObjectP\[{Model\[Instrument, MassSpectrometer\], Object\[Instrument, MassSpectrometer\]}\] | Automatic


#### **Detector**

The type of measurement to employ. Currently, we offer PhotoDiodeArray (measures the absorbance of a range of wavelengths) and MassSpectrometry (ionizes the analytes and measures the abundance of a given mass to charge ratio).

Default Value: {Temperature, Pressure, PhotoDiodeArray, MassSpectrometry}

Pattern Description: List of one or more Temperature, Pressure, PhotoDiodeArray, or MassSpectrometry entries or Temperature, Pressure, PhotoDiodeArray, or MassSpectrometry.

Programmatic Pattern: (Temperature | Pressure | PhotoDiodeArray | MassSpectrometry) | {(Temperature | Pressure | PhotoDiodeArray | MassSpectrometry)..}

#### **GuardColumn**

The protective device placed in the flow path before the Column in order to adsorb fouling contaminants, preserving the Column lifetime.

Default Value: Automatic

Default Calculation: Automatically set from the column model's PreferredGuardColumn. If Column is Null, GuardColumn resolves to Null too.

Pattern Description: An object of type or subtype Model\[Item, Column\], Object\[Item, Column\], Model\[Item, Cartridge, Column\], or Object\[Item, Cartridge, Column\] or Null.

Programmatic Pattern: (ObjectP\[{Model\[Item, Column\], Object\[Item, Column\], Model\[Item, Cartridge, Column\], Object\[Item, Cartridge, Column\]}\] | Automatic) | Null

#### **NumberOfReplicates**

The number of times to repeat measurements on each provided sample(s). If Aliquot -> True, this also indicates the number of times each provided sample will be aliquoted.

Default Value: Null

Pattern Description: Greater than 1 in increments of 1 or Null.

Programmatic Pattern: GreaterP\[1, 1\] | Null

#### **MaxAcceleration**

The maximum allowed change per time in FlowRate.

Default Value: Automatic

Default Calculation: Automatically set from the Column, Instrument, and GuardColumn models. The minimum MaxAcceleration will be used.

Pattern Description: Greater than 0 milliliters per minute squared or Null.

Programmatic Pattern: (GreaterP\[0\*(Milliliter/(Minute\*Minute))\] | Automatic) | Null

### Chromatography

#### **Column**

The item containing the stationary phase through which the buffers and input samples flow. It adsorbs and separates the molecules within the sample based on the properties of the mobile phase, samples, column material, and ColumnTemperature.

Default Value: Automatic

Default Calculation: Automatically set to a column model ideal for the specified SeparationMode.

Pattern Description: An object of type or subtype Model\[Item, Column\] or Object\[Item, Column\] or Null.

Programmatic Pattern: (ObjectP\[{Model\[Item, Column\], Object\[Item, Column\]}\] | Automatic) | Null

#### **SecondaryColumn**

An additional stationary phase through which the buffer and input samples flow. It is connected to flow path, downstream of the Column, and selectively adsorbs analytes.

Default Value: Automatic

Default Calculation: If ColumnSelector is specified, set from there; otherwise, set to Null.

Pattern Description: An object of type or subtype Model\[Item, Column\] or Object\[Item, Column\] or Null.

Programmatic Pattern: (ObjectP\[{Model\[Item, Column\], Object\[Item, Column\]}\] | Automatic) | Null

#### **TertiaryColumn**

An additional stationary phase through which the buffer and input samples flow. It is connected to flow path, downstream of the SecondaryColumn, and selectively adsorbs analytes.

Default Value: Automatic

Default Calculation: If ColumnSelector is specified, set from there; otherwise, set to Null.

Pattern Description: An object of type or subtype Model\[Item, Column\] or Object\[Item, Column\] or Null.

Programmatic Pattern: (ObjectP\[{Model\[Item, Column\], Object\[Item, Column\]}\] | Automatic) | Null

#### **ColumnSelector**

The list of all the columns loaded into the ChromatographyInstrument's column compartment or selector and referenced in GuardColumn, Column, SecondaryColumn, and TertiaryColumn options.

Default Value: Automatic

Default Calculation: Automatically set from the Column, SecondaryColumn, and TertiaryColumn options.

Pattern Description: {Guard Column, Column, Secondary Column, Tertiary Column} or Null.

Programmatic Pattern: ({ObjectP\[{Model\[Item, Column\], Object\[Item, Column\]}\] | (Automatic | Null), ObjectP\[{Model\[Item, Column\], Object\[Item, Column\]}\] | (Automatic | Null), ObjectP\[{Model\[Item, Column\], Object\[Item, Column\]}\] | (Automatic | Null), ObjectP\[{Model\[Item, Column\], Object\[Item, Column\]}\] | (Automatic | Null)} | Automatic) | Null

#### **ColumnTemperature**

The temperature of the Column throughout the measurement and/or collection.

Default Value: Automatic

Default Calculation: Automatically set from the temperature within the Gradient option; otherwise, Ambient temperature is used.

Pattern Description: Ambient or greater than or equal to 5 degrees Celsius and less than or equal to 80 degrees Celsius.

Programmatic Pattern: (RangeP\[5\*Celsius, 80\*Celsius\] | Ambient) | Automatic

Index Matches to: experiment samples

#### **BufferA**

The solvent pumped through channel A of the flow path.

Default Value: Automatic

Default Calculation: Automatically set from SeparationMode (e.g. Water buffer if ReversePhase) or the objects specified by the Gradient option.

Pattern Description: An object of type or subtype Object\[Sample\] or Model\[Sample\] or a prepared sample.

Programmatic Pattern: (ObjectP\[{Object\[Sample\], Model\[Sample\]}\] | \_String) | Automatic

#### **BufferB**

The solvent pumped through channel B of the flow path.

Default Value: Automatic

Default Calculation: Automatically set from SeparationMode (e.g. Acetonitrile buffer if ReversePhase) or the objects specified by the Gradient option.

Pattern Description: An object of type or subtype Object\[Sample\] or Model\[Sample\] or a prepared sample.

Programmatic Pattern: (ObjectP\[{Object\[Sample\], Model\[Sample\]}\] | \_String) | Automatic

#### **BufferC**

The solvent pumped through channel C of the flow path.

Default Value: Automatic

Default Calculation: Automatically set from SeparationMode or the objects specified by the Gradient option.

Pattern Description: An object of type or subtype Object\[Sample\] or Model\[Sample\] or a prepared sample.

Programmatic Pattern: (ObjectP\[{Object\[Sample\], Model\[Sample\]}\] | \_String) | Automatic

#### **BufferD**

The solvent pumped through channel D of the flow path.

Default Value: Automatic

Default Calculation: Automatically set from SeparationMode or the objects specified by the Gradient option.

Pattern Description: An object of type or subtype Object\[Sample\] or Model\[Sample\] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP\[{Object\[Sample\], Model\[Sample\]}\] | \_String) | Automatic) | Null

### Sample Parameters

#### **InjectionTable**

The order of sample, Standard, and Blank sample loading into the instrument during measurement and/or collection. This also includes the priming and flushing of the column.

Default Value: Automatic

Default Calculation: Determined to the order of input samples articulated. Standard and Blank samples are inserted based on the determination of StandardFrequency and BlankFrequency. For example, StandardFrequency -> FirstAndLast and BlankFrequency -> Null result in Standard samples injected first, then samples, and then the Standard sample set again.

Pattern Description: List of one or more {Type, Sample, InjectionVolume, Gradient, Mass Spectrometry} or {Type, Sample, InjectionVolume, Gradient, Mass Spectrometry} entries.

Programmatic Pattern: {({Standard | Sample | Blank, (ObjectP\[{Model\[Sample\], Object\[Sample\]}\] | \_String) | Automatic, RangeP\[0\*Microliter, 50\*Microliter, 1\*Microliter\] | Automatic, ObjectP\[Object\[Method, Gradient\]\] | (Automatic | New), ObjectP\[Object\[Method, MassAcquisition\]\] | (Automatic | New)} | {ColumnPrime | ColumnFlush, Automatic | Null, Automatic | Null, ObjectP\[Object\[Method, Gradient\]\] | (Automatic | New), ObjectP\[Object\[Method, MassAcquisition\]\] | (Automatic | New)})..} | Automatic

#### **SampleTemperature**

The temperature at which the samples, Standard, and Blank are kept in the instrument.

Default Value: Ambient

Pattern Description: Ambient or greater than or equal to 5 degrees Celsius and less than or equal to 40 degrees Celsius.

Programmatic Pattern: RangeP\[5\*Celsius, 40\*Celsius\] | Ambient

#### **InjectionVolume**

The physical quantity of sample loaded into the flow path for measurement.

Default Value: Automatic

Default Calculation: Set to 5 uL.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 50 microliters.

Programmatic Pattern: RangeP\[0\*Microliter, 50\*Microliter\] | Automatic

Index Matches to: experiment samples

#### **NeedleWashSolution**

The solvent used to wash the injection needle before each sample measurement.

Default Value: Automatic

Default Calculation: Set to 20% Methanol solution.

Pattern Description: An object of type or subtype Object\[Sample\] or Model\[Sample\] or a prepared sample.

Programmatic Pattern: (ObjectP\[{Object\[Sample\], Model\[Sample\]}\] | \_String) | Automatic

### Gradient

#### **GradientA**

The composition of BufferA within the flow, defined for specific time points. The composition is linearly interpolated for the intervening periods between the defined time points. For example for GradientA->{{0 Minute, 10 Percent},{30 Minute, 90 Percent}}, the percentage of BufferA in the flow will rise such that at 15 minutes, the composition should be 50\*Percent.

Default Value: Automatic

Default Calculation: Automatically set from Gradient option or implicitly resolved from GradientB, GradientC, and GradientD options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer A Composition} entries.

Programmatic Pattern: (RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic

Index Matches to: experiment samples

#### **GradientB**

The composition of BufferB within the flow, defined for specific time points. The composition is linearly interpolated for the intervening periods between the defined time points. For example for GradientB->{{0 Minute, 10 Percent},{30 Minute, 90 Percent}}, the percentage of BufferB in the flow will rise such that at 15 minutes, the composition should be 50\*Percent.

Default Value: Automatic

Default Calculation: Automatically set from Gradient option or implicitly resolved from GradientA, GradientC, and GradientD options. If no other gradient options are specified, a Buffer B gradient of 10% to 100% over 45 minutes is used.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer B Composition} entries.

Programmatic Pattern: (RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic

Index Matches to: experiment samples

#### **GradientC**

The composition of BufferC within the flow, defined for specific time points. The composition is linearly interpolated for the intervening periods between the defined time points. For example for GradientC->{{0 Minute, 10 Percent},{30 Minute, 90 Percent}}, the percentage of BufferC in the flow will rise such that at 15 minutes, the composition should be 50\*Percent.

Default Value: Automatic

Default Calculation: Automatically set from Gradient option or implicitly resolved from GradientA, GradientB, and GradientD options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer C Composition} entries.

Programmatic Pattern: (RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic

Index Matches to: experiment samples

#### **GradientD**

The composition of BufferD within the flow, defined for specific time points. The composition is linearly interpolated for the intervening periods between the defined time points. For example for GradientD->{{0 Minute, 10 Percent},{30 Minute, 90 Percent}}, the percentage of BufferD in the flow will rise such that at 15 minutes, the composition should be 50\*Percent.

Default Value: Automatic

Default Calculation: If the specified instrument supports Buffer D, this option automatically resolves from Gradient option or implicitly resolved from GradientA, GradientB, and GradientC options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer D Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

Index Matches to: experiment samples

#### **FlowRate**

The speed of the fluid through the pump. This speed is linearly interpolated such that consecutive entries of {Time, Flow Rate} will define the intervening fluid speed. For example, {{0 Minute, 0.3 Milliliter/Minute},{30 Minute, 0.5 Milliliter/Minute}} means the flow rate will be 0.4 Milliliter/Minute at 15 minutes into the run.

![](Files/ExperimentLCMS.en/I_10.png)

**Figure 3.1:** ESI source settings should be adjusted according to the flow rate used to infuse the sample into the mass spectrometer to ensure successful spray formation and solvent desolvation. This table provides recommended settings for typical flow rate ranges for both ESI-QTOF and ESI-QQQ. Note that ESI-QTOF and ESI-QQQ take different input ranges and units. Desolvation gas flow is input as gas flow rate for ESI-QTOF and gas pressure for ESI-QQQ; ESI-QQQ has different polarity for the capillary voltage for positive and negative ion mode, while ESI-QTOF only takes positive capillary voltage as the input.

Default Value: Automatic

Default Calculation: Automatically set from Type and Scale or inherited from the method given in the Gradient option.

Pattern Description: Greater than or equal to 0 milliliters per minute and less than or equal to 2 milliliters per minute or list of one or more {Time, Flow Rate} entries.

Programmatic Pattern: (RangeP\[(0\*Milliliter)/Minute, (2\*Milliliter)/Minute\] | {{GreaterEqualP\[0\*Minute\], RangeP\[(0\*Milliliter)/Minute, (2\*Milliliter)/Minute\]}..}) | Automatic

Index Matches to: experiment samples

#### **GradientStart**

A shorthand option to specify the starting BufferB composition in the fluid flow. This option must be specified with GradientEnd and GradientDuration.

Default Value: Null

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or Null.

Programmatic Pattern: RangeP\[0\*Percent, 100\*Percent\] | Null

Index Matches to: experiment samples

#### **GradientEnd**

A shorthand option to specify the final BufferB composition in the fluid flow. This option must be specified with GradientStart and GradientDuration.

Default Value: Null

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or Null.

Programmatic Pattern: RangeP\[0\*Percent, 100\*Percent\] | Null

Index Matches to: experiment samples

#### **GradientDuration**

A shorthand option to specify the duration of a gradient.

Default Value: Null

Pattern Description: Greater than or equal to 0 minutes or Null.

Programmatic Pattern: GreaterEqualP\[0\*Minute\] | Null

Index Matches to: experiment samples

#### **EquilibrationTime**

A shorthand option to specify the duration of equilibration at the starting buffer composition at the start of a gradient.

Default Value: Null

Pattern Description: Greater than or equal to 0 minutes or Null.

Programmatic Pattern: GreaterEqualP\[0\*Minute\] | Null

Index Matches to: experiment samples

#### **FlushTime**

A shorthand option to specify the duration of Buffer C flush at the end of a gradient.

Default Value: Null

Pattern Description: Greater than or equal to 0 minutes or Null.

Programmatic Pattern: GreaterEqualP\[0\*Minute\] | Null

Index Matches to: experiment samples

#### **Gradient**

The buffer composition over time in the fluid flow. Specific parameters of an object can be overridden by specific options.

Default Value: Automatic

Default Calculation: Automatically set to best meet all the Gradient options (e.g. GradientA, GradientB, GradientC, GradientD, FlowRate, GradientStart, GradientEnd, GradientDuration, EquilibrateTime, FlushTime).

Pattern Description: An object of type or subtype Object\[Method, Gradient\] or list of one or more {Time, Buffer A Composition, Buffer B Composition, Buffer C Composition, Buffer D Composition, Flow Rate} entries.

Programmatic Pattern: (ObjectP\[Object\[Method, Gradient\]\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[(0\*Milliliter)/Minute, (2\*Milliliter)/Minute\]}..}) | Automatic

Index Matches to: experiment samples

#### **StandardGradientStart**

A shorthand option to specify the starting BufferB composition in the fluid flow. This option must be specified with StandardGradientEnd and StandardGradientDuration.

Default Value: Null

Default Calculation: Automatically set to Null, if not specified.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or Null.

Programmatic Pattern: RangeP\[0\*Percent, 100\*Percent\] | Null

Index Matches to: Standard

#### **StandardGradientEnd**

A shorthand option to specify the final BufferB composition in the fluid flow. This option must be specified with StanadrdGradientStart and StamdardGradientDuration.

Default Value: Null

Default Calculation: Automatically set to Null, if not specified.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or Null.

Programmatic Pattern: RangeP\[0\*Percent, 100\*Percent\] | Null

Index Matches to: Standard

#### **StandardEquilibrationTime**

A shorthand option to specify the duration of constant buffer composition before the gradient changes.

Default Value: Null

Pattern Description: Greater than or equal to 0 minutes or Null.

Programmatic Pattern: GreaterEqualP\[0\*Minute\] | Null

Index Matches to: Standard

#### **StandardFlushTime**

A shorthand option to specify the duration of constant buffer composition after the gradient changes and before the next sample injection.

Default Value: Null

Pattern Description: Greater than or equal to 0 minutes or Null.

Programmatic Pattern: GreaterEqualP\[0\*Minute\] | Null

Index Matches to: Standard

#### **BlankGradientStart**

A shorthand option to specify the starting BufferB composition in the fluid flow. This option must be specified with BlankGradientEnd and BlankGradientDuration.

Default Value: Null

Default Calculation: Automatically set to Null, if not specified.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or Null.

Programmatic Pattern: RangeP\[0\*Percent, 100\*Percent\] | Null

Index Matches to: Blank

#### **BlankGradientEnd**

A shorthand option to specify the final BufferB composition in the fluid flow. This option must be specified with BlankGradientStart and BlankGradientDuration.

Default Value: Null

Default Calculation: Automatically set to Null, if not specified.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or Null.

Programmatic Pattern: RangeP\[0\*Percent, 100\*Percent\] | Null

Index Matches to: Blank

#### **BlankEquilibrationTime**

A shorthand option to specify the duration of constant buffer composition before the gradient changes.

Default Value: Null

Pattern Description: Greater than or equal to 0 minutes or Null.

Programmatic Pattern: GreaterEqualP\[0\*Minute\] | Null

Index Matches to: Blank

#### **BlankFlushTime**

A shorthand option to specify the duration of constant buffer composition after the gradient changes and before the next sample injection.

Default Value: Null

Pattern Description: Greater than or equal to 0 minutes or Null.

Programmatic Pattern: GreaterEqualP\[0\*Minute\] | Null

Index Matches to: Blank

### Mass Analysis

#### **Calibrant**

The sample with components of known mass-to-charge ratios (m/z) used to calibrate the mass spectrometer. In the chosen ion polarity mode, the calibrant should contain at least 3 masses spread over the mass range of interest.

![](Files/ExperimentLCMS.en/I_11.png)

**Figure 3.2:** Various calibrants available.

Default Value: Automatic

Default Calculation: If using QTOF as the mass analyzer, set to sodium iodide for peptide samples, cesium iodide for intact protein analysis. For other types of samples, is set to cesium iodide if molecular weight is above 2000 Da, to sodium iodide if molecular weight between 1200 and 2000 Da, and to sodium formate for all others (small molecule range). If using TripleQuadrupole as the mass analyzer, this option will be set automatically based on the first IonMode: Model\[Sample, "id:zGj91a71kXEO"\] or Model\[Sample, "id:bq9LA0JA1YJz"\] for Positive and Negative, respectively.

Pattern Description: An object of type or subtype Object\[Sample\] or Model\[Sample\] or a prepared sample.

Programmatic Pattern: (ObjectP\[{Object\[Sample\], Model\[Sample\]}\] | \_String) | Automatic

#### **SecondCalibrant**

The additional sample with components of known mass-to-charge ratios (m/z) used to calibrate the mass spectrometer. In the chosen ion polarity mode, the calibrant should contain at least 3 masses spread over the mass range of interest.

Default Value: Automatic

Default Calculation: Set to Model\[Sample, "id:zGj91a71kXEO"\] or Model\[Sample, "id:bq9LA0JA1YJz"\] for Positive and Negative, respectively, when using TripleQuandrupole as the MassAnalyzer. Otherwise set to Null.

Pattern Description: An object of type or subtype Object\[Sample\] or Model\[Sample\] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP\[{Object\[Sample\], Model\[Sample\]}\] | \_String) | Automatic) | Null

#### **Analytes**

The compounds of interest that are present in the given samples, used to determine the other settings for the Mass Spectrometer (ex. MassRange).

Default Value: Automatic

Default Calculation: If populated, will resolve to the user-specified Analytes field in the Object\[Sample\]. Otherwise, will resolve to the larger compounds in the sample, in the order of Proteins, Peptides, Oligomers, then other small molecules. Otherwise, set Null.

Pattern Description: List of one or more an object of type or subtype Model\[Molecule\], Model\[Molecule, cDNA\], Model\[Molecule, Oligomer\], Model\[Molecule, Transcript\], Model\[Molecule, Protein\], Model\[Molecule, Protein, Antibody\], Model\[Molecule, Carbohydrate\], Model\[Molecule, Polymer\], Model\[Resin\], Model\[Resin, SolidPhaseSupport\], Model\[Lysate\], Model\[ProprietaryFormulation\], Model\[Virus\], Model\[Cell\], Model\[Cell, Mammalian\], Model\[Cell, Bacteria\], Model\[Cell, Yeast\], Model\[Tissue\], Model\[Material\], or Model\[Species\] entries or Null.

Programmatic Pattern: ({ObjectP\[IdentityModelTypes\]..} | Automatic) | Null

Index Matches to: experiment samples

#### **IonMode**

Indicates if positively or negatively charged ions are analyzed.

Default Value: Automatic

Default Calculation: For oligomer samples of the types Peptide, DNA, and other synthetic oligomers, is automatically set to positive ion mode. For other types of samples, defaults to positive ion mode, unless the sample is acid (pH<=5 or pKa<=8).

Pattern Description: Negative or Positive.

Programmatic Pattern: IonModeP | Automatic

Index Matches to: experiment samples

#### **MassSpectrometryMethod**

The previously specified instruction(s) for the analyte ionization, selection, fragmentation, and detection.

Default Value: Automatic

Default Calculation: If set in the InjectionTable option, set to that; otherwise, set to New.

Pattern Description: An object of type or subtype Object\[Method, MassAcquisition\] or New or Null.

Programmatic Pattern: ((ObjectP\[Object\[Method, MassAcquisition\]\] | New) | Automatic) | Null

Index Matches to: experiment samples

#### **AcquisitionWindow**

The time range with respect to the chromatographic separation to conduct analyte ionization, selection/survey, optional fragmentation, and detection.

Default Value: Automatic

Default Calculation: Set to the entire gradient window 0 Minute to the last time point in Gradient.

Pattern Description: A span from anything greater than or equal to 0 minutes and less than or equal to 8 hours to anything greater than or equal to 0 minutes and less than or equal to 8 hours or list of one or more a span from anything greater than or equal to 0 minutes and less than or equal to 8 hours to anything greater than or equal to 0 minutes and less than or equal to 8 hours or {Automatic, Null} entries.

Programmatic Pattern: (RangeP\[0\*Minute, 8\*Hour\] ;; RangeP\[0\*Minute, 8\*Hour\] | {(RangeP\[0\*Minute, 8\*Hour\] ;; RangeP\[0\*Minute, 8\*Hour\] | (Automatic | Null))..}) | Automatic

Index Matches to: experiment samples

#### **AcquisitionMode**

The method by which spectra are collected. DataDependent will depend on the properties of the measured mass spectrum of the intact ions. DataIndependent will systemically scan through all of the intact ions. MS1 will focus on defined intact masses. MS1MS2 will focus on fragmented masses.

![](Files/ExperimentLCMS.en/I_12.png)

**Figure 3.3:** (a),(b) and (c):Various acquisition modes available for ExperimentLCMS using QTOF as the MassAnalyzer. For MS1FullScan mode, the collision cell is turned off, and ions are measured and resolved with just the quadrupole time of flight. For MS1FullScanMS2 mode, one intact mass (MassDetection) is selected in the first quadruple and disassociated into fragment ions with the collision cell. Fragment ions are resolved and detected with the quadrupole time of flight. For DataIndependent mode, scans are alternated between scanning a range of MS1FullScan masses (no fragmentation) and scanning fragmentation of a range of masses (MS2). For DataDependent mode, acquisition is split into cycles. For the first scan of each cycle, a survey is taken where the collision cell is off and only intact masses are measured. The top ranking intact ions are noted, then for each consequent scan of the cycle, a ranking intact ion is fragmented, and the resultant fragment ions are resolved and measured on the quadrupole time of flight. A suite of options are available to control how many ions are ranked, which ones are, and to eliminate redundancies. (d):Various mass spectrometry scan modes available for ExperimentLCMS using TripleQuad as the MassAnalyzer. In Full Scan Mode, the entire MS1 range is scanned and fragmentation is off. In SelectedIonMonitoring, select MS1 masses (per the MassDetection option) are monitored and measured without fragmentation. In PrecursorIonScan mode, fragmentation is on, and fragment ion is selected (per the FragmentMassDetection option), while MS1 masses are scanned across a range (MassDetection). In NeutralIonLoss mode, both MS1 and MS2 masses are scanned, to track specific MS1/MS2 combinations for neutral ion loss. In ProductIonScan, an MS1 mass is selected (MassDetection) and a range of MS2 mass is scanned to survey fragmentation patterns of the parent mass. In MultipleReactionMonitoring mode, both MS1 and MS2 are selected - specific intact and fragment ion pairs are monitored.

Default Value: Automatic

Default Calculation: Set to MS1FullScan unless DataDependent related options are set, then set to DataDependent.

Pattern Description: DataIndependent, DataDependent, MS1FullScan, MS1MS2ProductIonScan, SelectedIonMonitoring, NeutralIonLoss, PrecursorIonScan, or MultipleReactionMonitoring or list of one or more DataIndependent, DataDependent, MS1FullScan, MS1MS2ProductIonScan, SelectedIonMonitoring, NeutralIonLoss, PrecursorIonScan, or MultipleReactionMonitoring entries.

Programmatic Pattern: (MSAcquisitionModeP | {MSAcquisitionModeP..}) | Automatic

Index Matches to: experiment samples

#### **Fragment**

Indicates if ions should be collided with neutral gas and dissociated in order to measure the resulting product ions. Also known as tandem mass spectrometry or MS/MS (as opposed to MS).

Default Value: Automatic

Default Calculation: Set to True if AcquisitionMode is MS1MS2ProductIonScan, DataDependent, or DataIndependent. Set True if any of the Fragmentation related options are set (e.g. FragmentMassDetection).

Pattern Description: List of one or more True or False entries or True or False.

Programmatic Pattern: (BooleanP | {BooleanP..}) | Automatic

Index Matches to: experiment samples

#### **MassDetection**

The lowest and the highest mass-to-charge ratio (m/z) to be recorded or selected for intact masses. When Fragment is True, the intact ions will be selected for fragmentation.

![](Files/ExperimentLCMS.en/I_13.png)

**Figure 3.4:** MassDetection, IonMode, and Calibrant should be adjusted according to the type of analyte in the sample and the chosen ion mode. This table lists mass ranges and calibrants that this experiment automatically defaults to. For QTOF, the calibrant will be determined according to analyte types, if not user-specified: small molecules, peptides, and large molecules such as intact protein/antibodies and nucleic acid oligomers. For ESI-QQQ, the Calibrant and SecondCalibrant will be determined based on IonMode.

Default Value: Automatic

Default Calculation: For Fragment -> False, automatically set to one of three default mass ranges according to the molecular weight of the Analytes to encompass them.

Pattern Description: DataDependent or DataIndependent or MS1FullScan, NeutralIonLoss, DataDependent, DataIndependent or PrecursorIonScan or MS1MS2ProductIonScan or SelectedIonMonitoring or SelectedIonMonitoring or MultipleReactionMonitoring or list of one or more DataDependent or DataIndependent or MS1FullScan, NeutralIonLoss, DataDependent, DataIndependent or PrecursorIonScan or MS1MS2ProductIonScan or SelectedIonMonitoring or SelectedIonMonitoring or MultipleReactionMonitoring entries.

Programmatic Pattern: ((RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] ;; RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | {RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]..} | MSAnalyteGroupP) | {(RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] ;; RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | {RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]..} | MSAnalyteGroupP)..}) | Automatic

Index Matches to: experiment samples

#### **MassDetectionStepSize**

Indicate the step size for mass collection in range when using TripleQuadruploe as the MassAnalyzer.

Default Value: Automatic

Default Calculation: This option will be set to Null if using ESI-QTOF. For ESI-QQQ, if both of the mass anaylzer are in mass selection mode (SelectedIonMonitoring and MultipleReactionMonitoring mode), this option will be auto resolved to Null. In all other mass scan modes in ESI-QQQ, this option will be automatically resolved to 0.1 g/mol.

Pattern Description: Greater than or equal to 0.01 grams per mole and less than or equal to 1 gram per mole or list of one or more greater than or equal to 0.01 grams per mole and less than or equal to 1 gram per mole or Null entries or Null.

Programmatic Pattern: ((RangeP\[(0.01\*Gram)/Mole, (1\*Gram)/Mole\] | {(RangeP\[(0.01\*Gram)/Mole, (1\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **ScanTime**

The duration of time allowed to pass between each spectral acquisition. When AcquisitionMode is DataDependent, this value refers to the duration for measuring spectra from the intact ions. Increasing this value improves sensitivity whereas decreasing this value allows for more data points and spectra to be acquired.

Default Value: Automatic

Default Calculation: Set to 1 second unless a method is given.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 10 seconds or list of one or more greater than or equal to 0.015 seconds and less than or equal to 10 seconds entries.

Programmatic Pattern: (RangeP\[0.015\*Second, 10\*Second\] | {RangeP\[0.015\*Second, 10\*Second\]..}) | Automatic

Index Matches to: experiment samples

#### **FragmentMassDetection**

The lowest and the highest mass-to-charge ratio (m/z) to be recorded or selected for product ions. When AcquisitionMode is DataDependent|DataIndependent, all of the product ions in consideration for measurement. Null if Fragment is False.

Default Value: Automatic

Default Calculation: When Fragment is False, set to Null. Otherwise, 20 Gram/Mole to the maximum MassDetection.

Pattern Description: DataDependent or DataIndependent or MultipleReactionMonitoring or PrecursorIonScan or ProductIonScan or Null or list of one or more DataDependent or DataIndependent or MultipleReactionMonitoring or PrecursorIonScan or ProductIonScan or Null entries or Null.

Programmatic Pattern: ((({RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\]..} | RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\] ;; RangeP\[(100\*Gram)/Mole, (16000\*Gram)/Mole\] | All | Null | {RangeP\[(5\*Gram)/Mole, (2000\*Gram)/Mole\]..}) | {({RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\]..} | RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\] ;; RangeP\[(100\*Gram)/Mole, (16000\*Gram)/Mole\] | All | Null | {RangeP\[(5\*Gram)/Mole, (2000\*Gram)/Mole\]..})..}) | Automatic) | Null

Index Matches to: experiment samples

#### **CollisionEnergy**

The voltage by which intact ions are accelerated through inert gas in order to dissociate them into measurable fragment ion species when Fragment is True. CollisionEnergy cannot be defined simultaneously with CollisionEnergyMassProfile.

Default Value: Automatic

Default Calculation: Is automatically set to 40 Volt when Fragment is True, otherwise is set to Null.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 255 volts or greater than or equal to -180 volts and less than or equal to 5 volts or list of one or more A list of Single Values or Single Values or Null entries or Null.

Programmatic Pattern: (((RangeP\[0.1\*Volt, 255\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\]) | {((RangeP\[0.1\*Volt, 255\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\]) | {(RangeP\[5\*Volt, 180\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\])..} | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **CollisionCellExitVoltage**

Also known as the Collision Cell Exit Potential (CXP). This value focuses and accelerates the ions out of collision cell (Q2) and into 2nd mass analyzer (MS 2). This potential is tuned to ensure successful ion acceleration out of collision cell and into MS2, and can be adjusted to reach the maximal signal intensity. This option is unique to ESI-QQQ for now, and only required when Fragment ->True and/or in ScanMode that achieves tandem mass feature (PrecursorIonScan, NeutralIonLoss,MS1MS2ProductIonScan,MultipleReactionMonitoring). For non-tandem mass ScanMode (FullScan and SelectedIonMonitoring) and other massspectrometer (ESI-QTOF and MALDI-TOF), this option is resolved to Null.

Default Value: Automatic

Default Calculation: Is automatically set to 15 V (Positive mode) or -15 V (Negative mode) if the collision option is True and using QQQ as the mass analyzer.

Pattern Description: Greater than or equal to -55 volts and less than or equal to 55 volts or list of one or more greater than or equal to -55 volts and less than or equal to 55 volts or Null entries or Null.

Programmatic Pattern: ((RangeP\[-55\*Volt, 55\*Volt\] | {(RangeP\[-55\*Volt, 55\*Volt\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **DwellTime**

The duration of time for which spectra are acquired at the specific mass detection value for SelectedIonMonitoring and MultipleReactionMonitoring mode in ESI-QQQ.

Default Value: Automatic

Default Calculation: Is automatically set to 200 microsecond if StandardAcquisition is in SelectedIonMonitoring or MultipleReactionMonitoring mode. Otherwise is set to Null.

Pattern Description: Greater than or equal to 5 milliseconds and less than or equal to 2000 milliseconds or list of one or more greater than or equal to 5 milliseconds and less than or equal to 2000 milliseconds or Null entries or Null.

Programmatic Pattern: ((RangeP\[5\*Millisecond, 2000\*Millisecond\] | {(RangeP\[5\*Millisecond, 2000\*Millisecond\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **NeutralLoss**

A neutral loss scan is performed on ESI-QQQ instrument by scanning the sample through the first quadrupole (Q1). The ions are then fragmented in the collision cell. The second mass analyzer is then scanned with a fixed offset to MS1. This option represents the value of this offset.

Default Value: Automatic

Default Calculation: Is set to 500 g/mol if using NeutralIonLoss as AcquisitionMode, and is Null in other modes.

Pattern Description: Greater than 0 grams per mole or list of one or more greater than 0 grams per mole or Null entries or Null.

Programmatic Pattern: ((GreaterP\[(0\*Gram)/Mole\] | {(GreaterP\[(0\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **MultipleReactionMonitoringAssays**

In ESI-QQQ, the ion corresponding to the compound of interest is targetted with subsequent fragmentation of that target ion to produce a range of daughter ions. One (or more) of these fragment daughter ions can be selected for quantitation purposes. Only compounds that meet both these criteria, i.e. specific parent ion and specific daughter ions corresponding to the mass of the molecule of interest are detected within the mass spectrometer. The mass assays (MS1/MS2 mass value combinations) for each scan, along with the CollisionEnergy and DwellTime (length of time of each scan).

Default Value: Automatic

Default Calculation: Is set based one MassDetection, CollissionEnergy, DwellTime and FramentMassDetection.

Pattern Description: List of one or more list of one or more Individual Multiple Reaction Monitoring Assay or None entries or Null entries or Null or Null.

Programmatic Pattern: (({({({GreaterP\[(0\*Gram)/Mole\], (RangeP\[5\*Volt, 180\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\]) | Automatic, GreaterP\[(0\*Gram)/Mole\], GreaterP\[0\*Second\] | Automatic} | Null)..} | Null)..} | Null) | Automatic) | Null

Index Matches to: experiment samples

#### **CollisionEnergyMassProfile**

The relationship of collision energy with the MassDetection.

Default Value: Automatic

Default Calculation: Set to CollisionEnergyMassScan if defined; otherwise, set to Null.

Pattern Description: A span from anything greater than or equal to 0.1 volts and less than or equal to 255 volts to anything greater than or equal to 0.1 volts and less than or equal to 255 volts or list of one or more a span from anything greater than or equal to 0.1 volts and less than or equal to 255 volts to anything greater than or equal to 0.1 volts and less than or equal to 255 volts or Null entries or Null.

Programmatic Pattern: ((RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\] | {(RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **CollisionEnergyMassScan**

The collision energy profile at the end of the scan from CollisionEnergy or CollisionEnergyScanProfile, as related to analyte mass.

Default Value: Automatic

Pattern Description: A span from anything greater than or equal to 0.1 volts and less than or equal to 255 volts to anything greater than or equal to 0.1 volts and less than or equal to 255 volts or list of one or more a span from anything greater than or equal to 0.1 volts and less than or equal to 255 volts to anything greater than or equal to 0.1 volts and less than or equal to 255 volts or Null entries or Null.

Programmatic Pattern: ((RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\] | {(RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **SurveyChargeStateExclusion**

Indicates if redundant ions that differ by ionic charge (+1/-1, +2/-2, etc.) should be excluded and if ChargeState exclusion-related options should be automatically filled in.

Default Value: Automatic

Default Calculation: Set to True, if any of the ChargeState options are set; otherwise, False.

Pattern Description: List of one or more True or False or Null entries or True or False or Null.

Programmatic Pattern: ((BooleanP | {(BooleanP | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **SurveyIsotopeExclusion**

Indicates if redundant ions that differ by isotopic mass (e.g. 1, 2 Gram/Mole) should be exlcuded and if MassIsotope exclusion-related options should be automatically filled in.

Default Value: Automatic

Default Calculation: Set to True, if any of the IsotopeExclusion options are set; otherwise, False.

Pattern Description: List of one or more True or False or Null entries or True or False or Null.

Programmatic Pattern: ((BooleanP | {(BooleanP | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

### Ionization

#### **ESICapillaryVoltage**

The absolute voltage applied to the tip of the stainless steel capillary tubing in order to produce charged droplets. Adjust this voltage to maximize sensitivity. Most compounds are optimized between 0.5 and 3.2 kV in ESI positive ion mode and 0.5 and 2.6 in ESI negative ion mode, but can be altered according to sample type. For low flow applications, best sensitivity will be achieved with a relatively high value in ESI positive (e.g. 3.0 kV), for standard flow UPLC a value of 0.5 kV is typically best for maximum sensitivity.

Default Value: Automatic

Default Calculation: Is automatically set according to the flow rate (0-0.02 ml/min -> 3.0 kV, 0.02-0.1 ml/min -> 1.5 kV, >0.1 ml/min -> 0.5 kV).

Pattern Description: Greater than or equal to -4 kilovolts and less than or equal to 5 kilovolts.

Programmatic Pattern: RangeP\[-4\*Kilovolt, 5\*Kilovolt\] | Automatic

Index Matches to: experiment samples

#### **DeclusteringVoltage**

The voltage offset between the ion block (the reduced pressure chamber of the source block) and the stepwave ion guide (the optics before the quadrupole mass analyzer). This voltage attracts charged ions in the spray being produced from the capillary tip into the ion block leading into the mass spectrometer. This voltage is typically set to 25-100 V and its tuning has little effect on sensitivity compared to other options (e.g. StepwaveVoltage).

Default Value: Automatic

Default Calculation: Is automatically set to any specified MassAcquisition method; otherwise, set to 40 Volt.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 150 volts.

Programmatic Pattern: RangeP\[0.1\*Volt, 150\*Volt\] | Automatic

Index Matches to: experiment samples

#### **StepwaveVoltage**

The voltage offset between the 1st and 2nd stage of the ion guide which leads ions coming from the sample cone towards the quadrupole mass analyzer. This voltage normally optimizes between 25 and 150 V and should be adjusted for sensitivity depending on compound and charge state. For multiply charged species it is typically set to to 40-50 V, and higher for singly charged species. In general higher cone voltages (120-150 V) are needed for larger mass ions such as intact proteins and monoclonal antibodies. It also has greatest effect on in-source fragmentation and should be decreased if in-source fragmentation is observed but not desired. This is an unique option for QTOF as the massanalyzer.

Default Value: Automatic

Default Calculation: Is automatically set according to the sample type (proteins, antibodies and analytes with MW > 2000 -> 120 V, DNA and synthetic nucleic acid oligomers -> 100 V, all others (including peptides and small molecules) -> 40 V).

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 200 volts.

Programmatic Pattern: RangeP\[0.1\*Volt, 200\*Volt\] | Automatic

Index Matches to: experiment samples

#### **SourceTemperature**

The temperature setting of the source block. Heating the source block discourages condensation and decreases solvent clustering in the reduced vacuum region of the source. This temperature setting is flow rate and sample dependent. Typical values are between 60 to 120 Celsius. For thermally labile analytes, a lower temperature setting is recommended.

Default Value: Automatic

Default Calculation: Is automatically set according to the flow rate (0-0.02 ml/min -> 100 Celsius, 0.02-0.3 ml/min -> 120 Celsius, >0.301 -> 150 Celsius).

Pattern Description: Greater than or equal to 25 degrees Celsius and less than or equal to 150 degrees Celsius.

Programmatic Pattern: RangeP\[25\*Celsius, 150\*Celsius\] | Automatic

Index Matches to: experiment samples

#### **DesolvationTemperature**

The temperature setting for the ESI desolvation heater that controls the nitrogen gas temperature used for solvent evaporation to produce single gas phase ions from the ion spray. Similar to DesolvationGasFlow, this setting is dependent on solvent flow rate and composition. A typical range is 150 to 650 Celsius.

Default Value: Automatic

Default Calculation: Is automatically set according to the flow rate (0-0.02 ml/min -> 200 Celsius, 0.02-0.1 ml/min -> 350 Celsius, 0.101-0.3 -> 450 Celsius, 0.301->0.5 ml/min -> 500 Celsius, >0.500 ml/min -> 600 Celsius).

Pattern Description: Greater than or equal to 20 degrees Celsius and less than or equal to 650 degrees Celsius.

Programmatic Pattern: RangeP\[20\*Celsius, 650\*Celsius\] | Automatic

Index Matches to: experiment samples

#### **DesolvationGasFlow**

The rate at which nitrogen gas is flowed around the ESI capillary. It is used for solvent evaporation to produce single gas phase ions from the ion spray. Similar to DesolvationTemperature, this setting is dependent on solvent flow rate and composition. Higher desolvation gas flows usually result in increased sensitivity, but too high values can cause spray instability. Typical values are between 300 and 1200 L/h.

Default Value: Automatic

Default Calculation: Is automatically set according to the flow rate (0-0.02 ml/min -> 600 L/h, 0.02-0.3 ml/min -> 800 L/h, 0.301-0.500 ml/min -> 1000 L/h, >0.500 ml/min -> 1200 L/h).

Pattern Description: Greater than or equal to 55 liters per hour and less than or equal to 1200 liters per hour or greater than or equal to 0 pounds‐force per inch squared and less than or equal to 85 pounds‐force per inch squared.

Programmatic Pattern: (RangeP\[(55\*Liter)/Hour, (1200\*Liter)/Hour\] | RangeP\[0\*PSI, 85\*PSI\]) | Automatic

Index Matches to: experiment samples

#### **ConeGasFlow**

The nitrogen gas flow ejected around the sample inlet cone (the spherical metal plate acting as a first gate between the sprayer and the reduced pressure chamber, the ion block). This gas flow is used to minimize the formation of solvent ion clusters. It also helps reduce adduct ions and directing the spray into the ion block while keeping the sample cone clean. The same parameter is referred to as Curtain Gas Pressure for ESI-QQQ. Typical values are between 0 and 150 L/h for ESI-QTOF or 20 to 55 PSI for ESI-QQQ.

Default Value: Automatic

Default Calculation: Is automatically set to 50 Liter/Hour for ESI-QTOF and 50 PSI for ESI-QQQ, and is set to Null in MALDI-TOF. Is not recommended to set to a smaller value of 40 PSI in ESI-QQQ, due to potential deposition of the sample inside the instrument that will lead to contamination.

Pattern Description: Greater than or equal to 0 liters per hour and less than or equal to 300 liters per hour or greater than or equal to 30 pounds‐force per inch squared and less than or equal to 55 pounds‐force per inch squared.

Programmatic Pattern: (RangeP\[(0\*Liter)/Hour, (300\*Liter)/Hour\] | RangeP\[30\*PSI, 55\*PSI\]) | Automatic

Index Matches to: experiment samples

#### **IonGuideVoltage**

This option (also known as Entrance Potential (EP)) is a unique option of ESI-QQQ. This parameter indicates electric potential applied to the Ion Guide in ESI-QQQ, which guides and focuses the ions through the high-pressure ion guide region.

Default Value: Automatic

Default Calculation: Is automatically set to 10 V for positive ions, or –10 V for negative ions in ESI-QQQ, and can be changed between 2-15 V in both positive and negative mode. This value is set to Null in ESI-QTOF.

Pattern Description: Greater than or equal to -15 volts and less than or equal to -2 volts or greater than or equal to 2 volts and less than or equal to 15 volts or Null.

Programmatic Pattern: ((RangeP\[-15\*Volt, -2\*Volt\] | RangeP\[2\*Volt, 15\*Volt\]) | Automatic) | Null

Index Matches to: experiment samples

#### **StandardIonGuideVoltage**

This option (also known as Entrance Potential (EP)) is a unique option of ESI-QQQ. This parameter indicates electric potential applied to the Ion Guide in ESI-QQQ, which guides and focuses the ions through the high-pressure ion guide region.

Default Value: Automatic

Default Calculation: Is automatically set to the first IonGuideVoltage.

Pattern Description: Greater than or equal to -15 volts and less than or equal to -2 volts or greater than or equal to 2 volts and less than or equal to 15 volts or Null.

Programmatic Pattern: ((RangeP\[-15\*Volt, -2\*Volt\] | RangeP\[2\*Volt, 15\*Volt\]) | Automatic) | Null

Index Matches to: Standard

#### **BlankIonGuideVoltage**

This option (also known as Entrance Potential (EP)) is a unique option of ESI-QQQ. This parameter indicates electric potential applied to the Ion Guide in ESI-QQQ, which guides and focuses the ions through the high-pressure ion guide region.

Default Value: Automatic

Default Calculation: Is automatically set to the first IonGuideVoltage.

Pattern Description: Greater than or equal to -15 volts and less than or equal to -2 volts or greater than or equal to 2 volts and less than or equal to 15 volts or Null.

Programmatic Pattern: ((RangeP\[-15\*Volt, -2\*Volt\] | RangeP\[2\*Volt, 15\*Volt\]) | Automatic) | Null

Index Matches to: Blank

#### **ColumnPrimeIonGuideVoltage**

This option (also known as Entrance Potential (EP)) is a unique option of ESI-QQQ. This parameter indicates electric potential applied to the Ion Guide in ESI-QQQ, which guides and focuses the ions through the high-pressure ion guide region.

Default Value: Automatic

Default Calculation: Is automatically set to first IonGuideVoltage.

Pattern Description: Greater than or equal to -15 volts and less than or equal to -2 volts or greater than or equal to 2 volts and less than or equal to 15 volts or Null.

Programmatic Pattern: ((RangeP\[-15\*Volt, -2\*Volt\] | RangeP\[2\*Volt, 15\*Volt\]) | Automatic) | Null

#### **ColumnFlushIonGuideVoltage**

This option (also known as Entrance Potential (EP)) is a unique option of ESI-QQQ. This parameter indicates electric potential applied to the Ion Guide in ESI-QQQ, which guides and focuses the ions through the high-pressure ion guide region.

Default Value: Automatic

Default Calculation: Is automatically set to first IonGuideVoltage.

Pattern Description: Greater than or equal to -15 volts and less than or equal to -2 volts or greater than or equal to 2 volts and less than or equal to 15 volts or Null.

Programmatic Pattern: ((RangeP\[-15\*Volt, -2\*Volt\] | RangeP\[2\*Volt, 15\*Volt\]) | Automatic) | Null

### Data Dependent Acquisition

#### **FragmentScanTime**

The duration of the spectral scanning for each fragmentation of an intact ion when AcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Automatically set to the same value as ScanTime if AcquisitionMode is DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 10 seconds or list of one or more greater than or equal to 0.015 seconds and less than or equal to 10 seconds or Null entries or Null.

Programmatic Pattern: ((RangeP\[0.015\*Second, 10\*Second\] | {(RangeP\[0.015\*Second, 10\*Second\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **AcquisitionSurvey**

The number of intact ions to consider for fragmentation and product ion measurement in every measurement cycle when AcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Automatically set to 10 if AcquisitionMode is set to DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 1 and less than or equal to 30 in increments of 1 or list of one or more greater than or equal to 1 and less than or equal to 30 in increments of 1 or Null entries or Null.

Programmatic Pattern: ((RangeP\[1, 30, 1\] | {(RangeP\[1, 30, 1\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **MinimumThreshold**

The minimum number of total ions detected within ScanTime durations needed to trigger the start of data dependent acquisition when AcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Automatically set to (100000/Second)\*ScanTime if AcquisitionMode is DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or list of one or more greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or Null entries or Null.

Programmatic Pattern: ((RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | {(RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **AcquisitionLimit**

The maximum number of total ions for a specific intact ion when AcquisitionMode is set to DataDependent. When this value is exceeded, acquisition will switch to fragmentation of the next candidate ion.

Default Value: Automatic

Default Calculation: Automatically inherited from supplied method if AcquisitionMode is set to DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or list of one or more greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or Null entries or Null.

Programmatic Pattern: ((RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | {(RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **CycleTimeLimit**

The maximum possible computed duration of all of the scans for the intact and fragmentation measurements when AcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Calculated from the AcquisitionSurvey, ScanTime, and FragmentScanTime.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 20000 seconds or list of one or more greater than or equal to 0.015 seconds and less than or equal to 20000 seconds or Null entries or Null.

Programmatic Pattern: ((RangeP\[0.015\*Second, 20000\*Second\] | {(RangeP\[0.015\*Second, 20000\*Second\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **ExclusionDomain**

The time range when the ExclusionMasses are omitted in the chromatogram. Full indicates for the entire period.

Default Value: Automatic

Default Calculation: Set to the entire AcquisitionWindow.

Pattern Description: A span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or Null entries or list of one or more list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full entries entries or Null.

Programmatic Pattern: (((GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full) | {(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full | Null)..} | {{(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full)..}..}) | Automatic) | Null

Index Matches to: experiment samples

#### **ExclusionMass**

The intact ions (Target Mass) to omit. When set to All, the mass is excluded for the entire ExclusionDomain. When set to Once, the mass is excluded in the first survey appearance, but considered for consequent ones.

Default Value: Automatic

Default Calculation: If any ExclusionMode-related options are set (e.g. ExclusionMassTolerance), a target mass of the first Analyte (if not in InclusionMasses) is chosen and retention time is set to 0\*Minute.

Pattern Description: List of one or more list of one or more {Mode, Target Mass} entries entries or list of one or more {Mode, Target Mass} or Null entries or {Mode, Target Mass} or Null.

Programmatic Pattern: (({All | Once, RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]} | {({All | Once, RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]} | Null)..} | {{{All | Once, RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]}..}..}) | Automatic) | Null

Index Matches to: experiment samples

#### **ExclusionMassTolerance**

The range above and below each ion in ExclusionMasses to consider for omission when ExclusionMass is set to All or Once.

Default Value: Automatic

Default Calculation: If ExclusionMass -> All or Once, set to 0.5 Gram/Mole; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | {(RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **ExclusionRetentionTimeTolerance**

The range of time above and below the ExclusionDomain to consider for exclusion.

Default Value: Automatic

Default Calculation: If ExclusionMass and ExclusionDomain options are set, this is set to 10 seconds; otherwise, Null.

Pattern Description: Greater than or equal to 0 seconds and less than or equal to 3600 seconds or list of one or more greater than or equal to 0 seconds and less than or equal to 3600 seconds or Null entries or Null.

Programmatic Pattern: ((RangeP\[0\*Second, 3600\*Second\] | {(RangeP\[0\*Second, 3600\*Second\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **InclusionDomain**

The time range when InclusionMass applies in the chromatogram. Full indicates for the entire period.

Default Value: Automatic

Default Calculation: Set to the entire AcquisitionWindow.

Pattern Description: A span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or Null entries or list of one or more list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full entries entries or Null.

Programmatic Pattern: (((GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full) | {(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full | Null)..} | {{(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full)..}..}) | Automatic) | Null

Index Matches to: experiment samples

#### **InclusionMass**

The ions (Target Mass) to prioritize during the survey scan for further fragmentation when AcquisitionMode is DataDependent. When the Mode is Only, the InclusionMass will solely be considered for surveys. When Mode is Preferential, the InclusionMass will be prioritized for survey.

Default Value: Automatic

Default Calculation: When InclusionMode Only or Preferential, an entry mass is added based on the mass of the most salient analyte of the sample.

Pattern Description: List of one or more list of one or more {Mode, Target Mass} entries entries or list of one or more {Mode, Target Mass} or Null entries or {Mode, Target Mass} or Null.

Programmatic Pattern: (({Only | Preferential, RangeP\[(2\*Gram)/Mole, (4000\*Gram)/Mole\]} | {({Only | Preferential, RangeP\[(2\*Gram)/Mole, (4000\*Gram)/Mole\]} | Null)..} | {{{Only | Preferential, RangeP\[(2\*Gram)/Mole, (4000\*Gram)/Mole\]}..}..}) | Automatic) | Null

Index Matches to: experiment samples

#### **InclusionCollisionEnergy**

The overriding collision energy value that can be applied to the InclusionMass. Null will default to the CollisionEnergy and related options.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0 volts and less than or equal to 255 volts or list of one or more greater than or equal to 0 volts and less than or equal to 255 volts or Null entries or list of one or more list of one or more greater than or equal to 0 volts and less than or equal to 255 volts entries entries or Null.

Programmatic Pattern: ((RangeP\[0\*Volt, 255\*Volt\] | {(RangeP\[0\*Volt, 255\*Volt\] | Null)..} | {{RangeP\[0\*Volt, 255\*Volt\]..}..}) | Automatic) | Null

Index Matches to: experiment samples

#### **InclusionDeclusteringVoltage**

The overriding source voltage value that can be applied to the the InclusionMass. Null will default to the DeclusteringVoltage option.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 150 volts or list of one or more greater than or equal to 0.1 volts and less than or equal to 150 volts or Null entries or list of one or more list of one or more greater than or equal to 0.1 volts and less than or equal to 150 volts entries entries or Null.

Programmatic Pattern: ((RangeP\[0.1\*Volt, 150\*Volt\] | {(RangeP\[0.1\*Volt, 150\*Volt\] | Null)..} | {{RangeP\[0.1\*Volt, 150\*Volt\]..}..}) | Automatic) | Null

Index Matches to: experiment samples

#### **InclusionChargeState**

The maximum charge state of the InclusionMass to also consider for inclusion. For example, if this is set to 3 and the polarity is Positive, then +1,+2,+3 charge states will be considered as well.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0 and less than or equal to 6 in increments of 1 or list of one or more greater than or equal to 0 and less than or equal to 6 in increments of 1 or Null entries or list of one or more list of one or more greater than or equal to 0 and less than or equal to 6 in increments of 1 entries entries or Null.

Programmatic Pattern: ((RangeP\[0, 6, 1\] | {(RangeP\[0, 6, 1\] | Null)..} | {{RangeP\[0, 6, 1\]..}..}) | Automatic) | Null

Index Matches to: experiment samples

#### **InclusionScanTime**

The overriding scan time duration that can be applied to the the InclusionMass for the consequent fragmentation. Null will default to the FragmentScanTime option.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 10 seconds or list of one or more greater than or equal to 0.015 seconds and less than or equal to 10 seconds or Null entries or list of one or more list of one or more greater than or equal to 0.015 seconds and less than or equal to 10 seconds entries entries or Null.

Programmatic Pattern: ((RangeP\[0.015\*Second, 10\*Second\] | {(RangeP\[0.015\*Second, 10\*Second\] | Null)..} | {{RangeP\[0.015\*Second, 10\*Second\]..}..}) | Automatic) | Null

Index Matches to: experiment samples

#### **InclusionMassTolerance**

The range above and below each ion in InclusionMasses to consider for prioritization. For example, if set to 0.5 Gram/Mole, the total range is 1 Gram/Mole.

Default Value: Automatic

Default Calculation: Set to 0.5 Gram/Mole if InclusionMass is given; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | {(RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **ChargeStateExclusionLimit**

The number of ions to survey first with exclusion by ionic state. For example, if AcquisitionSurvey is 10 and this option is 5, then 5 ions will be surveyed with charge-state exclusion. For candidate ions of rank 6 to 10, no exclusion will be performed.

Default Value: Automatic

Default Calculation: Inherited from any supplied method; otherwise, set the same to AcquisitionSurvey, if any ChargeState option is set.

Pattern Description: Greater than or equal to 0 and less than or equal to 30 in increments of 1 or list of one or more greater than or equal to 0 and less than or equal to 30 in increments of 1 or Null entries or Null.

Programmatic Pattern: ((RangeP\[0, 30, 1\] | {(RangeP\[0, 30, 1\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **ChargeStateExclusion**

The specific ionic states of intact ions to redundantly exclude from the survey for further fragmentation/acquisition. 1 refers to +1/-1, 2 refers to +2/-2, etc.

Default Value: Automatic

Default Calculation: When SurveyChargeStateExclusion is True, set to {1,2}; otherwise, Null.

Pattern Description: Greater than or equal to 1 and less than or equal to 6 in increments of 1 or list of one or more greater than or equal to 1 and less than or equal to 6 in increments of 1 or Null entries or Null.

Programmatic Pattern: ((RangeP\[1, 6, 1\] | {(RangeP\[1, 6, 1\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **ChargeStateMassTolerance**

The range of m/z to consider for exclusion by ionic state property when SurveyChargeStateExclusion is True.

Default Value: Automatic

Default Calculation: When SurveyChargeStateExclusion is True, set to 0.5 Gram/Mole; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | {(RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **IsotopicExclusion**

The m/z difference between monoisotopic ions as a criterion for survey exclusion.

Default Value: Automatic

Default Calculation: When SurveyIsotopeExclusion is True, set to 1 Gram/Mole; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null entries or list of one or more list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole entries entries or Null.

Programmatic Pattern: (((Alternatives\[RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\]\]) | {(RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Null)..} | {{(Alternatives\[RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\]\])..}..}) | Automatic) | Null

Index Matches to: experiment samples

#### **IsotopeRatioThreshold**

The minimum relative magnitude between monoisotopic ions in order to be considered an isotope for exclusion.

Default Value: Automatic

Default Calculation: When SurveyIsotopeExclusion is True, set to 0.1; otherwise, Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or list of one or more greater than or equal to 0 and less than or equal to 1 or Null entries or list of one or more list of one or more greater than or equal to 0 and less than or equal to 1 entries entries or Null.

Programmatic Pattern: ((RangeP\[0, 1\] | {(RangeP\[0, 1\] | Null)..} | {{RangeP\[0, 1\]..}..}) | Automatic) | Null

Index Matches to: experiment samples

#### **IsotopeDetectionMinimum**

The acquisition rate of a given intact mass to consider for isotope exclusion in the survey.

Default Value: Automatic

Default Calculation: When SurveyIsotopeExclusion is True, set to 10 1/Second; otherwise, Null.

Pattern Description: Greater than or equal to 0 reciprocal seconds or list of one or more greater than or equal to 0 reciprocal seconds or Null entries or list of one or more list of one or more greater than or equal to 0 reciprocal seconds entries entries or Null.

Programmatic Pattern: ((GreaterEqualP\[(0\*1)/Second\] | {(GreaterEqualP\[(0\*1)/Second\] | Null)..} | {{GreaterEqualP\[(0\*1)/Second\]..}..}) | Automatic) | Null

Index Matches to: experiment samples

#### **IsotopeMassTolerance**

The range of m/z around a mass to consider for exclusion. This applies for both ChargeState and mass shifted Isotope. If set to 0.5 Gram/Mole, then the total range should be 1 Gram/Mole.

Default Value: Automatic

Default Calculation: When SurveyIsotopeExclusion or SurveyChargeStateExclusion is True, set to 0.5 Gram/Mole; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | {(RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

#### **IsotopeRatioTolerance**

The range of relative magnitude around IsotopeRatio to consider for isotope exclusion.

Default Value: Automatic

Default Calculation: If SurveyIsotopeExclusion is True, set to 30\*Percent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more greater than or equal to 0 percent and less than or equal to 100 percent or Null entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {(RangeP\[0\*Percent, 100\*Percent\] | Null)..}) | Automatic) | Null

Index Matches to: experiment samples

### Detector Parameters

#### **AbsorbanceWavelength**

The physical properties of light passed through the flow for measurement with the PhotoDiodeArray (PDA) Detector.

Default Value: Automatic

Default Calculation: When conducting absorbance measurement, set to All.

Pattern Description: All or Range or Single or Null.

Programmatic Pattern: ((RangeP\[190\*Nanometer, 500\*Nanometer\] | All | RangeP\[190\*Nanometer, 500\*Nanometer\] ;; RangeP\[200\*Nanometer, 500\*Nanometer\]) | Automatic) | Null

Index Matches to: experiment samples

#### **WavelengthResolution**

The increment of wavelength for the range of light passed through the flow for absorbance measurement with the photo diode array (PDA) detector.

Default Value: Automatic

Default Calculation: Automatically set to 1.2\*Nanometer. Set to Null if AbsorbanceWavelength is a singleton value.

Pattern Description: Greater than or equal to 1.2 nanometers and less than or equal to 12. nanometers or Null.

Programmatic Pattern: (RangeP\[1.2\*Nanometer, 12.\*Nanometer\] | Automatic) | Null

Index Matches to: experiment samples

#### **UVFilter**

Indicates if UV wavelengths (less than 210 nm) should be blocked from being transmitted through the sample for PhotoDiodeArray detectors.

Default Value: Automatic

Default Calculation: Automatically set to False for Instruments with PDA detectors; otherwise, resolves to Null.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

#### **AbsorbanceSamplingRate**

The frequency of measurement for the input sample(s). Lower values will be less susceptible to noise but will record less frequently across time.

Default Value: Automatic

Default Calculation: Automatically set to 20\*1/Second for Instruments with PhotoDiodeArray (PDA) detectors; otherwise, resolves to Null.

Pattern Description: Greater than or equal to 1 reciprocal second and less than or equal to 80 reciprocal seconds in increments of 1 reciprocal second or Null.

Programmatic Pattern: (RangeP\[(1\*1)/Second, (80\*1)/Second, (1\*1)/Second\] | Automatic) | Null

Index Matches to: experiment samples

### Standard

#### **Standard**

The reference compound(s) injected into the instrument, often used for quantification or to check internal measurement consistency.

Default Value: Automatic

Default Calculation: Automatically set from Type when any other Standard option is specified, otherwise resolves to Null.

Pattern Description: An object of type or subtype Model\[Sample\] or Object\[Sample\] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP\[{Model\[Sample\], Object\[Sample\]}\] | \_String) | Automatic) | Null

Index Matches to: Standard

#### **StandardInjectionVolume**

The quantity of each Standard loaded into the flow path for measurements.

Default Value: Automatic

Default Calculation: Automatically set from InjectionVolume.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 500 microliters or Null.

Programmatic Pattern: (RangeP\[0\*Microliter, 500\*Microliter\] | Automatic) | Null

Index Matches to: Standard

#### **StandardFrequency**

The frequency at which Standard measurements will be inserted among samples.

Default Value: Automatic

Default Calculation: Automatically set to FirstAndLast when any Standard options are specified.

Pattern Description: Greater than 0 in increments of 1 or None, First, Last, FirstAndLast, or GradientChange or Null.

Programmatic Pattern: (((None | First | Last | FirstAndLast | GradientChange) | GreaterP\[0, 1\]) | Automatic) | Null

#### **StandardColumnTemperature**

The temperature of the column when the Standard gradient and measurement are run.

Default Value: Automatic

Default Calculation: Automatically set from ColumnTemperature. Automatic resolution can be inherited from the StandardGradient option.

Pattern Description: Ambient or greater than or equal to 5 degrees Celsius and less than or equal to 80 degrees Celsius or Null.

Programmatic Pattern: ((RangeP\[5\*Celsius, 80\*Celsius\] | Ambient) | Automatic) | Null

Index Matches to: Standard

#### **StandardGradientA**

The composition of BufferA within the flow, defined for specific time points for Standard measurement.

Default Value: Automatic

Default Calculation: Automatically set from StandardGradient option or implicitly resolved from StandardGradientB, StandardGradientC, and StandardGradientD options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer A Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardGradientB**

The composition of BufferB within the flow, defined for specific time points for Standard measurement.

Default Value: Automatic

Default Calculation: Automatically set from StandardGradient option or implicitly resolved from StandardGradientA, StandardGradientC, and StandardGradientD options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer B Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardGradientC**

The composition of BufferC within the flow, defined for specific time points for Standard measurement.

Default Value: Automatic

Default Calculation: Automatically set from StandardGradient option or implicitly resolved from StandardGradientA, StandardGradientB, and StandardGradientD options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer C Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardGradientD**

The composition of BufferD within the flow, defined for specific time points for Standard measurement.

Default Value: Automatic

Default Calculation: Automatically set from StandardGradient option or implicitly resolved from StandardGradientA, StandardGradientB, and StandardGradientC options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer D Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardFlowRate**

The speed of the fluid through the system for Standard measurement.

Default Value: Automatic

Default Calculation: Automatically set from Type and Scale or inherited from the method given in the StandardGradient option.

Pattern Description: Greater than or equal to 0 milliliters per minute and less than or equal to 2 milliliters per minute or list of one or more {Time, Flow Rate} entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Milliliter)/Minute, (2\*Milliliter)/Minute\] | {{GreaterEqualP\[0\*Minute\], RangeP\[(0\*Milliliter)/Minute, (2\*Milliliter)/Minute\]}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardGradientDuration**

A shorthand option to specify the duration of the Standard gradient.

Default Value: Null

Pattern Description: Greater than or equal to 0 minutes or Null.

Programmatic Pattern: GreaterEqualP\[0\*Minute\] | Null

Index Matches to: Standard

#### **StandardGradient**

The buffer composition over time in the fluid flow for Standard measurement.

Default Value: Automatic

Default Calculation: Automatically set to best meet all the StandardGradient\_ options (e.g. StandardGradientA, StandardGradientB, StandardGradientC, StandardGradientD, StandardGradientDuration,).

Pattern Description: An object of type or subtype Object\[Method, Gradient\] or list of one or more {Time, Buffer A Composition, Buffer B Composition, Buffer C Composition, Buffer D Composition, Flow Rate} entries or Null.

Programmatic Pattern: ((ObjectP\[Object\[Method, Gradient\]\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[(0\*Milliliter)/Minute, (2\*Milliliter)/Minute\]}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardAnalytes**

The compounds of interest that are present in the given Standard, used to determine the other settings for the Mass Spectrometer (ex. MassRange).

Default Value: Automatic

Default Calculation: If populated, will resolve to the user-specified Analytes field in the Object\[Sample\]. Otherwise, will resolve to the larger compounds in the sample, in the order of Proteins, Peptides, Oligomers, then other small molecules; otherwise, set Null.

Pattern Description: List of one or more an object of type or subtype Model\[Molecule\], Model\[Molecule, cDNA\], Model\[Molecule, Oligomer\], Model\[Molecule, Transcript\], Model\[Molecule, Protein\], Model\[Molecule, Protein, Antibody\], Model\[Molecule, Carbohydrate\], Model\[Molecule, Polymer\], Model\[Resin\], Model\[Resin, SolidPhaseSupport\], Model\[Lysate\], Model\[ProprietaryFormulation\], Model\[Virus\], Model\[Cell\], Model\[Cell, Mammalian\], Model\[Cell, Bacteria\], Model\[Cell, Yeast\], Model\[Tissue\], Model\[Material\], or Model\[Species\] entries or Null.

Programmatic Pattern: ({ObjectP\[IdentityModelTypes\]..} | Automatic) | Null

Index Matches to: Standard

#### **StandardIonMode**

Indicates if positively or negatively charged ions are analyzed for the Standard.

Default Value: Automatic

Default Calculation: Set to the first IonMode for an analyte input sample.

Pattern Description: Negative or Positive or Null.

Programmatic Pattern: (IonModeP | Automatic) | Null

Index Matches to: Standard

#### **StandardMassSpectrometryMethod**

The previously specified instruction(s) for the Standard ionization, selection, fragmentation, and detection.

Default Value: Automatic

Default Calculation: If Standard samples exist and MassSpectrometryMethod is specified, then set to the first available StandardMassSpectrometryMethod.

Pattern Description: An object of type or subtype Object\[Method, MassAcquisition\] or Null.

Programmatic Pattern: (ObjectP\[Object\[Method, MassAcquisition\]\] | Automatic) | Null

Index Matches to: Standard

#### **StandardESICapillaryVoltage**

The absolute voltage applied to the tip of the stainless steel capillary tubing in order to produce charged droplets. Adjust this voltage to maximize sensitivity. Most compounds are optimized between 0.5 and 3.2 kV in ESI positive ion mode and 0.5 and 2.6 in ESI negative ion mode, but can be altered according to sample type. For low flow applications, best sensitivity will be achieved with a relatively high value in ESI positive (e.g. 3.0 kV), for standard flow UPLC a value of 0.5 kV is typically best for maximum sensitivity.

Default Value: Automatic

Default Calculation: Is automatically set to the first ESICapillaryVoltage.

Pattern Description: Greater than or equal to -4 kilovolts and less than or equal to 5 kilovolts or Null.

Programmatic Pattern: (RangeP\[-4\*Kilovolt, 5\*Kilovolt\] | Automatic) | Null

Index Matches to: Standard

#### **StandardDeclusteringVoltage**

The voltage offset between the ion block (the reduced pressure chamber of the source block) and the stepwave ion guide (the optics before the quadrupole mass analyzer). This voltage attracts charged ions in the spray being produced from the capillary tip into the ion block leading into the mass spectrometer. This voltage is typically set to 25-100 V and its tuning has little effect on sensitivity compared to other options (e.g. StandardStepwaveVoltage).

Default Value: Automatic

Default Calculation: Is automatically set to any specified MassAcquisition method; otherwise, set to 40 Volt.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 150 volts or Null.

Programmatic Pattern: (RangeP\[0.1\*Volt, 150\*Volt\] | Automatic) | Null

Index Matches to: Standard

#### **StandardStepwaveVoltage**

The voltage offset between the 1st and 2nd stage of the stepwave ion guide which leads ions coming from the sample cone towards the quadrupole mass analyzer. This voltage normally optimizes between 25 and 150 V and should be adjusted for sensitivity depending on compound and charge state. For multiply charged species it is typically set to to 40-50 V, and higher for singly charged species. In general higher cone voltages (120-150 V) are needed for larger mass ions such as intact proteins and monoclonal antibodies. It also has greatest effect on in-source fragmentation and should be decreased if in-source fragmentation is observed but not desired.

Default Value: Automatic

Default Calculation: Is automatically set to the first StepwaveVoltage.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 200 volts or Null.

Programmatic Pattern: (RangeP\[0.1\*Volt, 200\*Volt\] | Automatic) | Null

Index Matches to: Standard

#### **StandardSourceTemperature**

The temperature setting of the source block. Heating the source block discourages condensation and decreases solvent clustering in the reduced vacuum region of the source. This temperature setting is flow rate and sample dependent. Typical values are between 60 to 120 Celsius. For thermally labile analytes, a lower temperature setting is recommended.

Default Value: Automatic

Default Calculation: Is automatically set to the first SourceTemperature.

Pattern Description: Greater than or equal to 25 degrees Celsius and less than or equal to 150 degrees Celsius or Null.

Programmatic Pattern: (RangeP\[25\*Celsius, 150\*Celsius\] | Automatic) | Null

Index Matches to: Standard

#### **StandardDesolvationTemperature**

The temperature setting for the ESI desolvation heater that controls the nitrogen gas temperature used for solvent evaporation to produce single gas phase ions from the ion spray. Similar to StandardDesolvationGasFlow, this setting is dependent on solvent flow rate and composition. A typical range is from 150 to 650 Celsius.

Default Value: Automatic

Default Calculation: Is automatically set to the first DesolvationTemperature.

Pattern Description: Greater than or equal to 20 degrees Celsius and less than or equal to 650 degrees Celsius or Null.

Programmatic Pattern: (RangeP\[20\*Celsius, 650\*Celsius\] | Automatic) | Null

Index Matches to: Standard

#### **StandardDesolvationGasFlow**

The rate at which nitrogen gas is flowed around the ESI capillary. It is used for solvent evaporation to produce single gas phase ions from the ion spray. Similar to StandardDesolvationTemperature, this setting is dependent on solvent flow rate and composition. Higher desolvation temperatures usually result in increased sensitivity, but too high values can cause spray instability. Typical values are between 300 to 1200 L/h.

Default Value: Automatic

Default Calculation: Is automatically set to the first DesolvationGasFlow.

Pattern Description: Greater than or equal to 55 liters per hour and less than or equal to 1200 liters per hour or greater than or equal to 0 pounds‐force per inch squared and less than or equal to 85 pounds‐force per inch squared or Null.

Programmatic Pattern: ((RangeP\[(55\*Liter)/Hour, (1200\*Liter)/Hour\] | RangeP\[0\*PSI, 85\*PSI\]) | Automatic) | Null

Index Matches to: Standard

#### **StandardConeGasFlow**

The rate at which nitrogen gas is flowed around the sample inlet cone (the spherical metal plate acting as a first gate between the sprayer and the reduced pressure chamber, the ion block). This gas flow is used to minimize the formation of solvent ion clusters. It also helps reduce adduct ions and directing the spray into the ion block while keeping the sample cone clean. Typical values are between 0 and 150 L/h.

Default Value: Automatic

Default Calculation: Is automatically set to the first ConeGasFlow.

Pattern Description: Greater than or equal to 0 liters per hour and less than or equal to 300 liters per hour or greater than or equal to 30 pounds‐force per inch squared and less than or equal to 55 pounds‐force per inch squared or Null.

Programmatic Pattern: ((RangeP\[(0\*Liter)/Hour, (300\*Liter)/Hour\] | RangeP\[30\*PSI, 55\*PSI\]) | Automatic) | Null

Index Matches to: Standard

#### **StandardAcquisitionWindow**

The time range with respect to the the chromatographic separation to conduct standard analyte ionization, selection/survey, optional fragmentation, and detection.

Default Value: Automatic

Default Calculation: Set to the entire gradient window 0 Minute to the last time point in StandardGradient.

Pattern Description: A span from anything greater than or equal to 0 minutes and less than or equal to 8 hours to anything greater than or equal to 0 minutes and less than or equal to 8 hours or list of one or more a span from anything greater than or equal to 0 minutes and less than or equal to 8 hours to anything greater than or equal to 0 minutes and less than or equal to 8 hours entries or Null.

Programmatic Pattern: ((RangeP\[0\*Minute, 8\*Hour\] ;; RangeP\[0\*Minute, 8\*Hour\] | {(Alternatives\[RangeP\[0\*Minute, 8\*Hour\] ;; RangeP\[0\*Minute, 8\*Hour\]\])..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardAcquisitionMode**

The method by which spectra are collected. DataDependent will depend on the properties of the measured mass spectrum of the intact ions. DataIndependent will systemically scan through all of the intact ions. MS1 will focus on defined intact masses. MS1MS2ProductIonScan will focus on fragmented masses.

Default Value: Automatic

Default Calculation: Set to MS1FullScan unless DataDependent related options are set, then set to DataDependent.

Pattern Description: DataIndependent, DataDependent, MS1FullScan, MS1MS2ProductIonScan, SelectedIonMonitoring, NeutralIonLoss, PrecursorIonScan, or MultipleReactionMonitoring or list of one or more DataIndependent, DataDependent, MS1FullScan, MS1MS2ProductIonScan, SelectedIonMonitoring, NeutralIonLoss, PrecursorIonScan, or MultipleReactionMonitoring entries or Null.

Programmatic Pattern: ((MSAcquisitionModeP | {MSAcquisitionModeP..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardFragment**

Indicates if ions should be collided with neutral gas and dissociated in order to measure the resulting product ions. Also known as tandem mass spectrometry or MS/MS (as opposed to MS).

Default Value: Automatic

Default Calculation: Set to True if StandardAcquisitionMode is MS1MS2ProductIonScan, DataDependent, or DataIndependent. Set True if any of the Fragmentation related options are set (e.g. StandardFragmentMassDetection).

Pattern Description: List of one or more True or False entries or True or False or Null.

Programmatic Pattern: ((BooleanP | {BooleanP..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardMassDetection**

The lowest and the highest mass-to-charge ratio (m/z) to be recorded or selected for intact masses. When StandardFragment is True, the intact ions will be selected for fragmentation.

Default Value: Automatic

Default Calculation: For StandardFragment -> False, automatically set to one of three default mass ranges according to the molecular weight of the StandardAnalytes to encompass them.

Pattern Description: All or Range or Single or Specific List or list of one or more All or Range or Single or Specific List entries or Null.

Programmatic Pattern: (((RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | {RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]..} | RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] ;; RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | MSAnalyteGroupP) | {(RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | {RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]..} | RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] ;; RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | MSAnalyteGroupP)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardScanTime**

The duration of time allowed to pass between each spectral acquisition. When StandardAcquisitionMode is DataDependent, this value refers to the duration for measuring spectra from the intact ions. Increasing this value improves sensitivity whereas decreasing this value allows for more data points and spectra to be acquired.

Default Value: Automatic

Default Calculation: Set to 0.2 seconds unless a method is given.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 10 seconds or list of one or more greater than or equal to 0.015 seconds and less than or equal to 10 seconds entries or Null.

Programmatic Pattern: ((RangeP\[0.015\*Second, 10\*Second\] | {RangeP\[0.015\*Second, 10\*Second\]..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardFragmentMassDetection**

The lowest and the highest mass-to-charge ratio (m/z) to be recorded or selected for product ions. When StandardAcquisitionMode is DataDependent|DataIndependent, all of the product ions in consideration for measurement. Null if StandardFragment is False.

Default Value: Automatic

Default Calculation: When StandardFragment is False, set to Null. Otherwise, 20 Gram/Mole to the maximum StandardMassDetection.

Pattern Description: All or Range or Specific or list of one or more All or Range or Specific or Null entries or Null.

Programmatic Pattern: ((({RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\]..} | All | RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\] ;; RangeP\[(100\*Gram)/Mole, (16000\*Gram)/Mole\]) | {({RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\]..} | All | Null | RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\] ;; RangeP\[(100\*Gram)/Mole, (16000\*Gram)/Mole\])..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardCollisionEnergy**

The voltage by which intact ions are accelerated through inert gas in order to dissociate them into measurable fragment ion species when StandardFragment is True. StandardCollisionEnergy cannot be defined simultaneously with StandardCollisionEnergyMassProfile.

Default Value: Automatic

Default Calculation: Is automatically set to 40 Volt when StandardFragment is True, otherwise is set to Null.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 255 volts or greater than or equal to -180 volts and less than or equal to 5 volts or list of one or more A list of Single Values or Single Values or Null entries or Null.

Programmatic Pattern: (((RangeP\[0.1\*Volt, 255\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\]) | {((RangeP\[0.1\*Volt, 255\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\]) | {(RangeP\[5\*Volt, 180\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\])..} | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardCollisionEnergyMassProfile**

The relationship of collision energy with the StandardMassDetection.

Default Value: Automatic

Default Calculation: Set to StandardCollisionEnergyMassScan if defined; otherwise, set to Null.

Pattern Description: A span from anything greater than or equal to 0.1 volts and less than or equal to 255 volts to anything greater than or equal to 0.1 volts and less than or equal to 255 volts or list of one or more a span from anything greater than or equal to 0.1 volts and less than or equal to 255 volts to anything greater than or equal to 0.1 volts and less than or equal to 255 volts or Null entries or Null.

Programmatic Pattern: ((RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\] | {(RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardCollisionEnergyMassScan**

The collision energy profile at the end of the scan from StandardCollisionEnergy or StandardCollisionEnergyScanProfile, as related to analyte mass.

Default Value: Automatic

Pattern Description: A span from anything greater than or equal to 0.1 volts and less than or equal to 255 volts to anything greater than or equal to 0.1 volts and less than or equal to 255 volts or list of one or more a span from anything greater than or equal to 0.1 volts and less than or equal to 255 volts to anything greater than or equal to 0.1 volts and less than or equal to 255 volts or Null entries or Null.

Programmatic Pattern: ((RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\] | {(RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardFragmentScanTime**

The duration of the spectral scanning for each fragmentation of an intact ion when StandardAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Automatically set to the same value as ScanTime if StandardAcquisitionMode is DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 10 seconds or list of one or more greater than or equal to 0.015 seconds and less than or equal to 10 seconds or Null entries or Null.

Programmatic Pattern: ((RangeP\[0.015\*Second, 10\*Second\] | {(RangeP\[0.015\*Second, 10\*Second\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardAcquisitionSurvey**

The number of intact ions to consider for fragmentation and product ion measurement in every measurement cycle when StandardAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Automatically set to 10 if StandardAcquisitionMode is set to DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 1 and less than or equal to 30 in increments of 1 or list of one or more greater than or equal to 1 and less than or equal to 30 in increments of 1 or Null entries or Null.

Programmatic Pattern: ((RangeP\[1, 30, 1\] | {(RangeP\[1, 30, 1\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardMinimumThreshold**

The minimum number of total ions detected within ScanTime durations needed to trigger the start of data dependent acquisition when StandardAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Automatically set to (100000/Second)\*ScanTime if StandardAcquisitionMode is DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or list of one or more greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or Null entries or Null.

Programmatic Pattern: ((RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | {(RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardAcquisitionLimit**

The maximum number of total ions for a specific intact ion when StandardAcquisitionMode is set to DataDependent. When this value is exceeded, acquisition will switch to fragmentation of the next candidate ion.

Default Value: Automatic

Default Calculation: Automatically inherited from supplied method if StandardAcquisitionMode is set to DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or list of one or more greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or Null entries or Null.

Programmatic Pattern: ((RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | {(RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardCycleTimeLimit**

The maximum possible computed duration of all of the scans for the intact and fragmentation measurements when StandardAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Calculated from the StandardAcquisitionSurvey, StandardScanTime, and StandardFragmentScanTime.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 20000 seconds or list of one or more greater than or equal to 0.015 seconds and less than or equal to 20000 seconds or Null entries or Null.

Programmatic Pattern: ((RangeP\[0.015\*Second, 20000\*Second\] | {(RangeP\[0.015\*Second, 20000\*Second\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardExclusionDomain**

The time range when the StandardExclusionMasses are omitted in the chromatogram. Full indicates for the entire period.

Default Value: Automatic

Default Calculation: Set to the entire StandardAcquisitionWindow.

Pattern Description: A span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or Null entries or list of one or more list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full entries entries or Null.

Programmatic Pattern: (((GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full) | {(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full | Null)..} | {{(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full)..}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardExclusionMass**

The intact ions (Target Mass) to omit. When set to All, the mass is excluded for the entire StandardExclusionDomain. When set to Once, the mass is excluded in the first survey appearance, but considered for consequent ones.

Default Value: Automatic

Default Calculation: If any StandardExclusionMode-related options are set (e.g. StandardExclusionMassTolerance), a target mass of the first Analyte (if not in StandardInclusionMasses) is chosen and retention time is set to 0\*Minute.

Pattern Description: List of one or more list of one or more {Mode, Target Mass} entries entries or list of one or more {Mode, Target Mass} or Null entries or {Mode, Target Mass} or Null.

Programmatic Pattern: (({All | Once, RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]} | {({All | Once, RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]} | Null)..} | {{{All | Once, RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]}..}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardExclusionMassTolerance**

The range above and below each ion in StandardExclusionMasses to consider for omission when StandardExclusionMass is All or Once.

Default Value: Automatic

Default Calculation: If StandardExclusionMass -> All or Once, set to 0.5 Gram/Mole; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | {(RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardExclusionRetentionTimeTolerance**

The range of time above and below the StandardExclusionDomain to consider for exclusion.

Default Value: Automatic

Default Calculation: If StandardExclusionMass and StandardExclusionDomain options are set, this is set to 10 seconds; otherwise, Null.

Pattern Description: Greater than or equal to 0 seconds and less than or equal to 3600 seconds or list of one or more greater than or equal to 0 seconds and less than or equal to 3600 seconds or Null entries or Null.

Programmatic Pattern: ((RangeP\[0\*Second, 3600\*Second\] | {(RangeP\[0\*Second, 3600\*Second\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardInclusionDomain**

The time range when StandardInclusionMass applies with respect to the chromatogram. Full indicates for the entire period.

Default Value: Automatic

Default Calculation: Set to the entire StandardAcquisitionWindow.

Pattern Description: A span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or Null entries or list of one or more list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full entries entries or Null.

Programmatic Pattern: (((GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full) | {(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full | Null)..} | {{(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full)..}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardInclusionMass**

The ions (Target Mass) to prioritize during the survey scan for further fragmentation when StandardAcquisitionMode is DataDependent. StandardInclusionMass set to Only will solely be considered for surveys. When Mode is Preferential, the InclusionMass will be prioritized for survey.

Default Value: Automatic

Default Calculation: When StandardInclusionMode Only or Preferential, an entry mass is added based on the mass of the most salient analyte of the sample.

Pattern Description: List of one or more list of one or more {Mode, Target Mass} entries entries or list of one or more {Mode, Target Mass} or Null entries or {Mode, Target Mass} or Null.

Programmatic Pattern: (({Only | Preferential, RangeP\[(2\*Gram)/Mole, (4000\*Gram)/Mole\]} | {({Only | Preferential, RangeP\[(2\*Gram)/Mole, (4000\*Gram)/Mole\]} | Null)..} | {{{Only | Preferential, RangeP\[(2\*Gram)/Mole, (4000\*Gram)/Mole\]}..}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardInclusionCollisionEnergy**

The overriding collision energy value that can be applied to the the StandardInclusionMass. Null will default to the StandardCollisionEnergy option and related options.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0 volts and less than or equal to 255 volts or list of one or more greater than or equal to 0 volts and less than or equal to 255 volts or Null entries or list of one or more list of one or more greater than or equal to 0 volts and less than or equal to 255 volts entries entries or Null.

Programmatic Pattern: ((RangeP\[0\*Volt, 255\*Volt\] | {(RangeP\[0\*Volt, 255\*Volt\] | Null)..} | {{RangeP\[0\*Volt, 255\*Volt\]..}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardInclusionDeclusteringVoltage**

The overriding source voltage value that can be applied to the the StandardInclusionMass. Null will default to the StandardDeclusteringVoltage option.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 150 volts or list of one or more greater than or equal to 0.1 volts and less than or equal to 150 volts or Null entries or list of one or more list of one or more greater than or equal to 0.1 volts and less than or equal to 150 volts entries entries or Null.

Programmatic Pattern: ((RangeP\[0.1\*Volt, 150\*Volt\] | {(RangeP\[0.1\*Volt, 150\*Volt\] | Null)..} | {{RangeP\[0.1\*Volt, 150\*Volt\]..}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardInclusionChargeState**

The maximum charge state of the StandardInclusionMass to also consider for inclusion. For example, if this is set to 3 and the polarity is Positive, then +1,+2,+3 charge states will be considered as well.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0 and less than or equal to 6 in increments of 1 or list of one or more greater than or equal to 0 and less than or equal to 6 in increments of 1 or Null entries or list of one or more list of one or more greater than or equal to 0 and less than or equal to 6 in increments of 1 entries entries or Null.

Programmatic Pattern: ((RangeP\[0, 6, 1\] | {(RangeP\[0, 6, 1\] | Null)..} | {{RangeP\[0, 6, 1\]..}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardInclusionScanTime**

The overriding scan time duration that can be applied to the the StandardInclusionMass for the consequent fragmentation. Null will default to the StandardFragmentScanTime option.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 10 seconds or list of one or more greater than or equal to 0.015 seconds and less than or equal to 10 seconds or Null entries or list of one or more list of one or more greater than or equal to 0.015 seconds and less than or equal to 10 seconds entries entries or Null.

Programmatic Pattern: ((RangeP\[0.015\*Second, 10\*Second\] | {(RangeP\[0.015\*Second, 10\*Second\] | Null)..} | {{RangeP\[0.015\*Second, 10\*Second\]..}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardInclusionMassTolerance**

The range above and below each ion in StandardInclusionMass to consider for prioritization. For example, if set to 0.5 Gram/Mole, the total range is 1 Gram/Mole.

Default Value: Automatic

Default Calculation: Set to 0.5 Gram/Mole if StandardInclusionMass is given; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | {(RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardSurveyChargeStateExclusion**

Indicates if redundant ions that differ by ionic charge (+1/-1, +2/-2, etc.) should be excluded and if StandardChargeState exclusion-related options should be automatically filled in.

Default Value: Automatic

Default Calculation: Set to True, if any of the StandardChargeState options are set; otherwise, False.

Pattern Description: List of one or more True or False or Null entries or True or False or Null.

Programmatic Pattern: ((BooleanP | {(BooleanP | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardSurveyIsotopeExclusion**

Indicates if redundant ions that differ by isotopic mass (e.g. 1, 2 Gram/Mole) should be excluded and if StandardMassIsotope exclusion-related options should be automatically filled in.

Default Value: Automatic

Default Calculation: Set to True, if any of the StandardIsotopeExclusion options are set; otherwise, False.

Pattern Description: List of one or more True or False or Null entries or True or False or Null.

Programmatic Pattern: ((BooleanP | {(BooleanP | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardChargeStateExclusionLimit**

The number of ions to survey first with exclusion by ionic state. For example, if StandardAcquisitionSurvey is 10 and this option is 5, then 5 ions will be surveyed with charge-state exclusion. For candidate ions of rank 6 to 10, no exclusion will be performed.

Default Value: Automatic

Default Calculation: Inherited from any supplied method; otherwise, set the same to StandardAcquisitionSurvey, if any ChargeState option is set.

Pattern Description: Greater than or equal to 0 and less than or equal to 30 in increments of 1 or list of one or more greater than or equal to 0 and less than or equal to 30 in increments of 1 or Null entries or Null.

Programmatic Pattern: ((RangeP\[0, 30, 1\] | {(RangeP\[0, 30, 1\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardChargeStateExclusion**

The specific ionic states of intact ions to redundantly exclude from the survey for further fragmentation/acquisition. 1 refers to +1/-1, 2 refers to +2/-2, etc.

Default Value: Automatic

Default Calculation: When StandardSurveyChargeStateExclusion is True, set to {1,2}; otherwise, Null.

Pattern Description: Greater than or equal to 1 and less than or equal to 6 in increments of 1 or list of one or more greater than or equal to 1 and less than or equal to 6 in increments of 1 or Null entries or Null.

Programmatic Pattern: ((RangeP\[1, 6, 1\] | {(RangeP\[1, 6, 1\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardChargeStateMassTolerance**

The range of m/z to consider for exclusion by ionic state property when StandardSurveyChargeStateExclusion is True.

Default Value: Automatic

Default Calculation: When StandardSurveyChargeStateExclusion is True, set to 0.5 Gram/Mole; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | {(RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardIsotopicExclusion**

The m/z difference between monoisotopic ions as a criterion for survey exclusion.

Default Value: Automatic

Default Calculation: When StandardSurveyIsotopeExclusion is True, set to 1 Gram/Mole; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null entries or list of one or more list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole entries entries or Null.

Programmatic Pattern: (((Alternatives\[RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\]\]) | {(RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Null)..} | {{(Alternatives\[RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\]\])..}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardIsotopeRatioThreshold**

The minimum relative magnitude between monoisotopic ions in order to be considered for exclusion.

Default Value: Automatic

Default Calculation: When StandardSurveyIsotopeExclusion is True, set to 0.1; otherwise, Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or list of one or more greater than or equal to 0 and less than or equal to 1 or Null entries or list of one or more list of one or more greater than or equal to 0 and less than or equal to 1 entries entries or Null.

Programmatic Pattern: ((RangeP\[0, 1\] | {(RangeP\[0, 1\] | Null)..} | {{RangeP\[0, 1\]..}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardIsotopeDetectionMinimum**

The acquisition rate of a given intact mass to consider for isotope exclusion in the survey.

Default Value: Automatic

Default Calculation: When StandardSurveyIsotopeExclusion is True, set to 10 1/Second; otherwise, Null.

Pattern Description: Greater than or equal to 0 reciprocal seconds or list of one or more greater than or equal to 0 reciprocal seconds or Null entries or list of one or more list of one or more greater than or equal to 0 reciprocal seconds entries entries or Null.

Programmatic Pattern: ((GreaterEqualP\[(0\*1)/Second\] | {(GreaterEqualP\[(0\*1)/Second\] | Null)..} | {{GreaterEqualP\[(0\*1)/Second\]..}..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardIsotopeMassTolerance**

The range of m/z around a mass to consider for exclusion. This applies for both ChargeState and mass shifted Isotope. If set to 0.5 Gram/Mole, then the total range should be 1 Gram/Mole.

Default Value: Automatic

Default Calculation: When StandardSurveyIsotopeExclusion or StandardSurveyChargeStateExclusion is True, set to 0.5 Gram/Mole; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | {(RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardIsotopeRatioTolerance**

The range of relative magnitude around StandardIsotopeRatio to consider for isotope exclusion.

Default Value: Automatic

Default Calculation: If StandardSurveyIsotopeExclusion is True, set to 30\*Percent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more greater than or equal to 0 percent and less than or equal to 100 percent or Null entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {(RangeP\[0\*Percent, 100\*Percent\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardDwellTime**

The duration of time for which spectra are acquired at the specific mass detection value for SelectedIonMonitoring and MultipleReactionMonitoring mode in ESI-QQQ.

Default Value: Automatic

Default Calculation: Is automatically set to 200 microsecond if StandardAcquisition is in SelectedIonMonitoring or MultipleReactionMonitoring mode. Otherwise is set to Null.

Pattern Description: Greater than or equal to 5 milliseconds and less than or equal to 2000 milliseconds or list of one or more greater than or equal to 5 milliseconds and less than or equal to 2000 milliseconds or Null entries or Null.

Programmatic Pattern: ((RangeP\[5\*Millisecond, 2000\*Millisecond\] | {(RangeP\[5\*Millisecond, 2000\*Millisecond\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardCollisionCellExitVoltage**

Also known as the Collision Cell Exit Potential (CXP). This value focuses and accelerates the ions out of collision cell (Q2) and into 2nd mass analyzer (MS 2). This potential is tuned to ensure successful ion acceleration out of collision cell and into MS2, and can be adjusted to reach the maximal signal intensity. This option is unique to ESI-QQQ for now, and only required when Fragment ->True and/or in ScanMode that achieves tandem mass feature (PrecursorIonScan, NeutralIonLoss,ProductIonScan,MultipleReactionMonitoring). For non-tandem mass ScanMode (FullScan and SelectedIonMonitoring) and other massspectrometer (ESI-QTOF and MALDI-TOF), this option is resolved to Null.

Default Value: Automatic

Default Calculation: For TripleQuandrupole as the MassAnalyzer, is set to first CollisionCellExitVoltage, otherwise set to Null.

Pattern Description: Greater than or equal to -55 volts and less than or equal to 55 volts or list of one or more greater than or equal to -55 volts and less than or equal to 55 volts or Null entries or Null.

Programmatic Pattern: ((RangeP\[-55\*Volt, 55\*Volt\] | {(RangeP\[-55\*Volt, 55\*Volt\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardMassDetectionStepSize**

Indicate the step size for mass collection in range when using TripleQuadruploe as the MassAnalyzer.

Default Value: Automatic

Default Calculation: Is set to first MassDetectionStepSize

Pattern Description: Greater than or equal to 0.01 grams per mole and less than or equal to 1 gram per mole or list of one or more greater than or equal to 0.01 grams per mole and less than or equal to 1 gram per mole or Null entries or Null.

Programmatic Pattern: ((RangeP\[(0.01\*Gram)/Mole, (1\*Gram)/Mole\] | {(RangeP\[(0.01\*Gram)/Mole, (1\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardNeutralLoss**

A neutral loss scan is performed on ESI-QQQ mass spectrometry by scanning the sample through the first quadrupole (Q1). The ions are then fragmented in the collision cell. The second mass analyzer is then scanned with a fixed offset to MS1. This option represents the value of this offset.

Default Value: Automatic

Default Calculation: Is set to 500 g/mol if using NeutralIonLoss as StandardAcquisitionMode, and is Null in other modes.

Pattern Description: Greater than 0 grams per mole or list of one or more greater than 0 grams per mole or Null entries or Null.

Programmatic Pattern: ((GreaterP\[(0\*Gram)/Mole\] | {(GreaterP\[(0\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: Standard

#### **StandardMultipleReactionMonitoringAssays**

In ESI-QQQ mass spectrometry analysis, the ion corresponding to the compound of interest is targetted with subsequent fragmentation of that target ion to produce a range of daughter ions. One (or more) of these fragment daughter ions can be selected for quantitation purposes. Only compounds that meet both these criteria, i.e. specific parent ion and specific daughter ions corresponding to the mass of the molecule of interest are detected within the mass spectrometer. The mass assays (MS1/MS2 mass value combinations) for each scan, along with the CollisionEnergy and DwellTime (length of time of each scan).

Default Value: Automatic

Default Calculation: Is set based one StandardMassDetection, StandardCollissionEnergy, StandardDwellTime and StandardFramentMassDetection.

Pattern Description: List of one or more list of one or more Individual Multiple Reaction Monitoring Assay or None entries or Null entries or Null or Null.

Programmatic Pattern: (({({({GreaterP\[(0\*Gram)/Mole\], (RangeP\[5\*Volt, 180\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\]) | Automatic, GreaterP\[(0\*Gram)/Mole\], GreaterP\[0\*Second\] | Automatic} | Null)..} | Null)..} | Null) | Automatic) | Null

Index Matches to: Standard

#### **StandardAbsorbanceWavelength**

The physical properties of light passed through the flow for Standard measurement with the PhotoDiodeArray (PDA) Detector.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in AbsorbanceWavelength.

Pattern Description: All or Range or Single or Null.

Programmatic Pattern: ((RangeP\[190\*Nanometer, 500\*Nanometer, 1\*Nanometer\] | All | RangeP\[190\*Nanometer, 490\*Nanometer, 1\*Nanometer\] ;; RangeP\[200\*Nanometer, 500\*Nanometer, 1\*Nanometer\]) | Automatic) | Null

Index Matches to: Standard

#### **StandardWavelengthResolution**

The increment of wavelength for the range of light passed through the flow for Standard absorbance measurement with the photo diode array (PDA) detector.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in WavelengthResolution.

Pattern Description: Greater than or equal to 1.2 nanometers and less than or equal to 12. nanometers or Null.

Programmatic Pattern: (RangeP\[1.2\*Nanometer, 12.\*Nanometer\] | Automatic) | Null

Index Matches to: Standard

#### **StandardUVFilter**

Indicates if UV wavelengths (less than 210 nm) should be blocked from being transmitted through the sample for the PhotoDiodeArray (PDA) detector for Standard measurement.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in UVFilter.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: Standard

#### **StandardAbsorbanceSamplingRate**

The frequency of Standard measurement. Lower values will be less susceptible to noise but will record less frequently across time.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in AbsorbanceSamplingRate.

Pattern Description: Greater than or equal to 1 reciprocal second and less than or equal to 80 reciprocal seconds in increments of 1 reciprocal second or Null.

Programmatic Pattern: (RangeP\[(1\*1)/Second, (80\*1)/Second, (1\*1)/Second\] | Automatic) | Null

Index Matches to: Standard

#### **StandardStorageCondition**

The non-default conditions under which any standards used by this experiment should be stored after the protocol is completed. If left unset, the standard samples will be stored according to their Models' DefaultStorageCondition.

Default Value: Null

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, BacteriaIncubation, MammalianIncubation, TissueCultureCellsIncubation, MicrobialCellsIncubation, MicrobialCellsShakingIncubation, YeastCellsIncubation, YeastCellsShakingIncubation, ViralIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: (Alternatives\[SampleStorageTypeP | Disposal\]) | Null

Index Matches to: Standard

### Blanks

#### **Blank**

The reference compound to inject into the instrument, often used for quantification or to check internal measurement consistency.

Default Value: Automatic

Default Calculation: Automatically set from Type when any other Blank option is specified, otherwise resolves to Null.

Pattern Description: An object of type or subtype Model\[Sample\] or Object\[Sample\] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP\[{Model\[Sample\], Object\[Sample\]}\] | \_String) | Automatic) | Null

Index Matches to: Blank

#### **BlankInjectionVolume**

The quantity of each Blank to load into the flow path for measurement.

Default Value: Automatic

Default Calculation: Automatically set from InjectionVolume.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 500 microliters or Null.

Programmatic Pattern: (RangeP\[0\*Microliter, 500\*Microliter\] | Automatic) | Null

Index Matches to: Blank

#### **BlankFrequency**

The frequency at which Blank measurements will be inserted among samples.

Default Value: Automatic

Default Calculation: Automatically set to FirstAndLast when any Blank options are specified.

Pattern Description: Greater than 0 in increments of 1 or None, First, Last, FirstAndLast, or GradientChange or Null.

Programmatic Pattern: (((None | First | Last | FirstAndLast | GradientChange) | GreaterP\[0, 1\]) | Automatic) | Null

#### **BlankColumnTemperature**

The temperature of the column when the Blank gradient and measurement are run.

Default Value: Automatic

Default Calculation: Automatically set from ColumnTemperature. Automatic resolution can be inherited from the BlankGradient option.

Pattern Description: Ambient or greater than or equal to 5 degrees Celsius and less than or equal to 80 degrees Celsius or Null.

Programmatic Pattern: ((RangeP\[5\*Celsius, 80\*Celsius\] | Ambient) | Automatic) | Null

Index Matches to: Blank

#### **BlankGradientA**

The composition of BufferA within the flow, defined for specific time points for Blank measurement.

Default Value: Automatic

Default Calculation: Automatically set from BlankGradient option or implicitly resolved from BlankGradientB, BlankGradientC, and BlankGradientD options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer A Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankGradientB**

The composition of BufferB within the flow, defined for specific time points for Blank measurement.

Default Value: Automatic

Default Calculation: Automatically set from BlankGradient option or implicitly resolved from BlankGradientA, BlankGradientC, and BlankGradientD options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer B Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankGradientC**

The composition of BufferC within the flow, defined for specific time points for Blank measurement.

Default Value: Automatic

Default Calculation: Automatically set from BlankGradient option or implicitly resolved from BlankGradientA, BlankGradientB, and BlankGradientD options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer C Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankGradientD**

The composition of BufferD within the flow, defined for specific time points for Blank measurement.

Default Value: Automatic

Default Calculation: Automatically set from BlankGradient option or implicitly resolved from BlankGradientA, BlankGradientB, and BlankGradientC options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer D Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankFlowRate**

The speed of the fluid through the system for Blank measurement.

Default Value: Automatic

Default Calculation: Automatically set from Type and Scale or inherited from the method given in the BlankGradient option.

Pattern Description: Greater than or equal to 0 milliliters per minute and less than or equal to 2 milliliters per minute or list of one or more {Time, Flow Rate} entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Milliliter)/Minute, (2\*Milliliter)/Minute\] | {{GreaterEqualP\[0\*Minute\], RangeP\[(0\*Milliliter)/Minute, (2\*Milliliter)/Minute\]}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankGradientDuration**

A shorthand option to specify the duration of the Blank gradient.

Default Value: Null

Pattern Description: Greater than or equal to 0 minutes or Null.

Programmatic Pattern: GreaterEqualP\[0\*Minute\] | Null

Index Matches to: Blank

#### **BlankGradient**

The buffer composition over time in the fluid flow for Blank measurement.

Default Value: Automatic

Default Calculation: Automatically set to best meet all the BlankGradient\_ options (e.g. BlankGradientA, BlankGradientB, BlankGradientC, BlankGradientD, BlankGradientDuration,).

Pattern Description: An object of type or subtype Object\[Method, Gradient\] or list of one or more {Time, Buffer A Composition, Buffer B Composition, Buffer C Composition, Buffer D Composition, Flow Rate} entries or Null.

Programmatic Pattern: ((ObjectP\[Object\[Method, Gradient\]\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[(0\*Milliliter)/Minute, (2\*Milliliter)/Minute\]}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankAnalytes**

The compounds of interest that are present in the given Blank samples, used to determine the other settings for the Mass Spectrometer (ex. MassRange).

Default Value: Automatic

Default Calculation: If populated, will resolve to the user-specified Analytes field in the Object\[Sample\]. Otherwise, will resolve to the larger compounds in the sample, in the order of Proteins, Peptides, Oligomers, then other small molecules. Otherwise, set Null.

Pattern Description: List of one or more an object of type or subtype Model\[Molecule\], Model\[Molecule, cDNA\], Model\[Molecule, Oligomer\], Model\[Molecule, Transcript\], Model\[Molecule, Protein\], Model\[Molecule, Protein, Antibody\], Model\[Molecule, Carbohydrate\], Model\[Molecule, Polymer\], Model\[Resin\], Model\[Resin, SolidPhaseSupport\], Model\[Lysate\], Model\[ProprietaryFormulation\], Model\[Virus\], Model\[Cell\], Model\[Cell, Mammalian\], Model\[Cell, Bacteria\], Model\[Cell, Yeast\], Model\[Tissue\], Model\[Material\], or Model\[Species\] entries or Null.

Programmatic Pattern: ({ObjectP\[IdentityModelTypes\]..} | Automatic) | Null

Index Matches to: Blank

#### **BlankIonMode**

Indicates if positively or negatively charged ions are analyzed.

Default Value: Automatic

Default Calculation: Set to the first IonMode for an analyte input sample.

Pattern Description: Negative or Positive or Null.

Programmatic Pattern: (IonModeP | Automatic) | Null

Index Matches to: Blank

#### **BlankMassSpectrometryMethod**

The previously specified instruction(s) for the analyte ionization, selection, fragmentation, and detection.

Default Value: Automatic

Default Calculation: If Blank samples exist and MassSpectrometryMethod is specified, then set to the first available BlankMassSpectrometryMethod.

Pattern Description: An object of type or subtype Object\[Method, MassAcquisition\] or Null.

Programmatic Pattern: (ObjectP\[Object\[Method, MassAcquisition\]\] | Automatic) | Null

Index Matches to: Blank

#### **BlankESICapillaryVoltage**

The absolute voltage applied to the tip of the stainless steel capillary tubing in order to produce charged droplets. Adjust this voltage to maximize sensitivity. Most compounds are optimized between 0.5 and 3.2 kV in ESI positive ion mode and 0.5 and 2.6 in ESI negative ion mode, but can be altered according to sample type. For low flow applications, best sensitivity will be achieved with a relatively high value in ESI positive (e.g. 3.0 kV), for blank flow UPLC a value of 0.5 kV is typically best for maximum sensitivity.

Default Value: Automatic

Default Calculation: Is automatically set to the first ESICapillaryVoltage.

Pattern Description: Greater than or equal to -4 kilovolts and less than or equal to 5 kilovolts or Null.

Programmatic Pattern: (RangeP\[-4\*Kilovolt, 5\*Kilovolt\] | Automatic) | Null

Index Matches to: Blank

#### **BlankDeclusteringVoltage**

The voltage offset between the ion block (the reduced pressure chamber of the source block) and the stepwave ion guide (the optics before the quadrupole mass analyzer). This voltage attracts charged ions in the spray being produced from the capillary tip into the ion block leading into the mass spectrometer. This voltage is typically set to 25-100 V and its tuning has little effect on sensitivity compared to other options (e.g. BlankStepwaveVoltage).

Default Value: Automatic

Default Calculation: Is automatically set to any specified MassAcquisition method; otherwise, set to 40 Volt.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 150 volts or Null.

Programmatic Pattern: (RangeP\[0.1\*Volt, 150\*Volt\] | Automatic) | Null

Index Matches to: Blank

#### **BlankStepwaveVoltage**

The voltage offset between the 1st and 2nd stage of the stepwave ion guide which leads ions coming from the sample cone towards the quadrupole mass analyzer. This voltage normally optimizes between 25 and 150 V and should be adjusted for sensitivity depending on compound and charge state. For multiply charged species it is typically set to to 40-50 V, and higher for singly charged species. In general higher cone voltages (120-150 V) are needed for larger mass ions such as intact proteins and monoclonal antibodies. It also has greatest effect on in-source fragmentation and should be decreased if in-source fragmentation is observed but not desired.

Default Value: Automatic

Default Calculation: Is automatically set to the first StepwaveVoltage.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 200 volts or Null.

Programmatic Pattern: (RangeP\[0.1\*Volt, 200\*Volt\] | Automatic) | Null

Index Matches to: Blank

#### **BlankSourceTemperature**

The temperature setting of the source block. Heating the source block discourages condensation and decreases solvent clustering in the reduced vacuum region of the source. This temperature setting is flow rate and sample dependent. Typical values are between 60 to 120 Celsius. For thermally labile analytes, a lower temperature setting is recommended.

Default Value: Automatic

Default Calculation: Is automatically set to the first SourceTemperature.

Pattern Description: Greater than or equal to 25 degrees Celsius and less than or equal to 150 degrees Celsius or Null.

Programmatic Pattern: (RangeP\[25\*Celsius, 150\*Celsius\] | Automatic) | Null

Index Matches to: Blank

#### **BlankDesolvationTemperature**

The temperature setting for the ESI desolvation heater that controls the nitrogen gas temperature used for solvent evaporation to produce single gas phase ions from the ion spray. Similar to BlankDesolvationGasFlow, this setting is dependent on solvent flow rate and composition. A typical range is from 150 to 650 Celsius.

Default Value: Automatic

Default Calculation: Is automatically set to the first DesolvationTemperature.

Pattern Description: Greater than or equal to 20 degrees Celsius and less than or equal to 650 degrees Celsius or Null.

Programmatic Pattern: (RangeP\[20\*Celsius, 650\*Celsius\] | Automatic) | Null

Index Matches to: Blank

#### **BlankDesolvationGasFlow**

The rate at which nitrogen gas is flowed around the ESI capillary. It is used for solvent evaporation to produce single gas phase ions from the ion spray. Similar to BlankDesolvationTemperature, this setting is dependent on solvent flow rate and composition. Higher desolvation temperatures usually result in increased sensitivity, but too high values can cause spray instability. Typical values are between 300 to 1200 L/h.

Default Value: Automatic

Default Calculation: Is automatically set to the first DesolvationGasFlow.

Pattern Description: Greater than or equal to 55 liters per hour and less than or equal to 1200 liters per hour or greater than or equal to 0 pounds‐force per inch squared and less than or equal to 85 pounds‐force per inch squared or Null.

Programmatic Pattern: ((RangeP\[(55\*Liter)/Hour, (1200\*Liter)/Hour\] | RangeP\[0\*PSI, 85\*PSI\]) | Automatic) | Null

Index Matches to: Blank

#### **BlankConeGasFlow**

The rate at which nitrogen gas is flowed around the sample inlet cone (the spherical metal plate acting as a first gate between the sprayer and the reduced pressure chamber, the ion block). This gas flow is used to minimize the formation of solvent ion clusters. It also helps reduce adduct ions and directing the spray into the ion block while keeping the sample cone clean. Typical values are between 0 and 150 L/h.

Default Value: Automatic

Default Calculation: Is automatically set to the first ConeGasFlow.

Pattern Description: Greater than or equal to 0 liters per hour and less than or equal to 300 liters per hour or greater than or equal to 30 pounds‐force per inch squared and less than or equal to 55 pounds‐force per inch squared or Null.

Programmatic Pattern: ((RangeP\[(0\*Liter)/Hour, (300\*Liter)/Hour\] | RangeP\[30\*PSI, 55\*PSI\]) | Automatic) | Null

Index Matches to: Blank

#### **BlankAcquisitionWindow**

The time range with respect to the the chromatographic separation to conduct analyte ionization, selection/survey, optional fragmentation, and detection.

Default Value: Automatic

Default Calculation: Set to the entire gradient window 0 Minute to the last time point in BlankGradient.

Pattern Description: A span from anything greater than or equal to 0 minutes and less than or equal to 8 hours to anything greater than or equal to 0 minutes and less than or equal to 8 hours or list of one or more a span from anything greater than or equal to 0 minutes and less than or equal to 8 hours to anything greater than or equal to 0 minutes and less than or equal to 8 hours entries or Null.

Programmatic Pattern: ((RangeP\[0\*Minute, 8\*Hour\] ;; RangeP\[0\*Minute, 8\*Hour\] | {(Alternatives\[RangeP\[0\*Minute, 8\*Hour\] ;; RangeP\[0\*Minute, 8\*Hour\]\])..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankAcquisitionMode**

The method by which spectra are collected. DataDependent will depend on the properties of the measured mass spectrum of the intact ions. DataIndependent will systemically scan through all of the intact ions. MS1 will focus on defined intact masses. MS1MS2 will focus on fragmented masses.

Default Value: Automatic

Default Calculation: Set to MS1FullScan unless DataDependent related options are set, then set to DataDependent.

Pattern Description: DataIndependent, DataDependent, MS1FullScan, MS1MS2ProductIonScan, SelectedIonMonitoring, NeutralIonLoss, PrecursorIonScan, or MultipleReactionMonitoring or list of one or more DataIndependent, DataDependent, MS1FullScan, MS1MS2ProductIonScan, SelectedIonMonitoring, NeutralIonLoss, PrecursorIonScan, or MultipleReactionMonitoring entries or Null.

Programmatic Pattern: ((MSAcquisitionModeP | {MSAcquisitionModeP..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankFragment**

Indicates if ions should be collided with neutral gas and dissociated in order to measure the resulting product ions. Also known as tandem mass spectrometry or MS/MS (as opposed to MS).

Default Value: Automatic

Default Calculation: Set to True if BlankAcquisitionMode is MS1MS2ProductIonScan, DataDependent, or DataIndependent. Set True if any of the Fragmentation related options are set (e.g. BlankFragmentMassDetection).

Pattern Description: List of one or more True or False entries or True or False or Null.

Programmatic Pattern: ((BooleanP | {BooleanP..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankMassDetection**

The lowest and the highest mass-to-charge ratio (m/z) to be recorded or selected for intact masses. When BlankFragment is True, the intact ions will be selected for fragmentation.

Default Value: Automatic

Default Calculation: For BlankFragment -> False, automatically set to one of three default mass ranges according to the molecular weight of the BlankAnalytes to encompass them.

Pattern Description: All or Range or Single or Specific List or list of one or more All or Range or Single or Specific List entries or Null.

Programmatic Pattern: (((RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | {RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]..} | RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] ;; RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | MSAnalyteGroupP) | {(RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | {RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]..} | RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] ;; RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | MSAnalyteGroupP)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankScanTime**

The duration of time allowed to pass between each spectral acquisition. When BlankAcquisitionMode is DataDependent, this value refers to the duration for measuring spectra from the intact ions. Increasing this value improves sensitivity whereas decreasing this value allows for more data points and spectra to be acquired.

Default Value: Automatic

Default Calculation: Set to 0.2 seconds unless a method is given.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 10 seconds or list of one or more greater than or equal to 0.015 seconds and less than or equal to 10 seconds entries or Null.

Programmatic Pattern: ((RangeP\[0.015\*Second, 10\*Second\] | {RangeP\[0.015\*Second, 10\*Second\]..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankFragmentMassDetection**

The lowest and the highest mass-to-charge ratio (m/z) to be recorded or selected for product ions. When BlankAcquisitionMode is DataDependent|DataIndependent, all of the product ions in consideration for measurement. Null if BlankFragment is False.

Default Value: Automatic

Default Calculation: When BlankFragment is False, set to Null. Otherwise, 20 Gram/Mole to the maximum BlankMassDetection.

Pattern Description: All or Range or Specific or list of one or more All or Range or Specific or Null entries or Null.

Programmatic Pattern: ((({RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\]..} | All | RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\] ;; RangeP\[(100\*Gram)/Mole, (16000\*Gram)/Mole\]) | {({RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\]..} | All | Null | RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\] ;; RangeP\[(100\*Gram)/Mole, (16000\*Gram)/Mole\])..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankCollisionEnergy**

The voltage by which intact ions are accelerated through inert gas in order to dissociate them into measurable fragment ion species when BlankFragment is True. BlankCollisionEnergy cannot be defined simultaneously with BlankCollisionEnergyMassProfile.

Default Value: Automatic

Default Calculation: Is automatically set to 40 Volt when BlankFragment is True, otherwise is set to Null.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 255 volts or greater than or equal to -180 volts and less than or equal to 5 volts or list of one or more A list of Single Values or Single Values or Null entries or Null.

Programmatic Pattern: (((RangeP\[0.1\*Volt, 255\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\]) | {((RangeP\[0.1\*Volt, 255\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\]) | {(RangeP\[5\*Volt, 180\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\])..} | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankCollisionEnergyMassProfile**

The relationship of collision energy with the BlankMassDetection.

Default Value: Automatic

Default Calculation: Set to BlankCollisionEnergyMassScan if defined; otherwise, set to Null.

Pattern Description: A span from anything greater than or equal to 0.1 volts and less than or equal to 255 volts to anything greater than or equal to 0.1 volts and less than or equal to 255 volts or list of one or more a span from anything greater than or equal to 0.1 volts and less than or equal to 255 volts to anything greater than or equal to 0.1 volts and less than or equal to 255 volts or Null entries or Null.

Programmatic Pattern: ((RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\] | {(RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankCollisionEnergyMassScan**

The collision energy profile at the end of the scan from BlankCollisionEnergy or BlankCollisionEnergyScanProfile, as related to analyte mass.

Default Value: Automatic

Pattern Description: A span from anything greater than or equal to 0.1 volts and less than or equal to 255 volts to anything greater than or equal to 0.1 volts and less than or equal to 255 volts or list of one or more a span from anything greater than or equal to 0.1 volts and less than or equal to 255 volts to anything greater than or equal to 0.1 volts and less than or equal to 255 volts or Null entries or Null.

Programmatic Pattern: ((RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\] | {(RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankFragmentScanTime**

The duration of the spectral scanning for each fragmentation of an intact ion when BlankAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Automatically set to the same value as ScanTime if BlankAcquisitionMode is DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 10 seconds or list of one or more greater than or equal to 0.015 seconds and less than or equal to 10 seconds or Null entries or Null.

Programmatic Pattern: ((RangeP\[0.015\*Second, 10\*Second\] | {(RangeP\[0.015\*Second, 10\*Second\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankAcquisitionSurvey**

The number of intact ions to consider for fragmentation and product ion measurement in every measurement cycle when BlankAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Automatically set to 10 if BlankAcquisitionMode is set to DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 1 and less than or equal to 30 in increments of 1 or list of one or more greater than or equal to 1 and less than or equal to 30 in increments of 1 or Null entries or Null.

Programmatic Pattern: ((RangeP\[1, 30, 1\] | {(RangeP\[1, 30, 1\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankMinimumThreshold**

The minimum number of total ions detected within ScanTime durations needed to trigger the start of data dependent acquisition when BlankAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Automatically set to (100000/Second)\*ScanTime if BlankAcquisitionMode is DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or list of one or more greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or Null entries or Null.

Programmatic Pattern: ((RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | {(RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankAcquisitionLimit**

The maximum number of total ions for a specific intact ion when BlankAcquisitionMode is set to DataDependent. When this value is exceeded, acquisition will switch to fragmentation of the next candidate ion.

Default Value: Automatic

Default Calculation: Automatically inherited from supplied method if BlankAcquisitionMode is set to DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or list of one or more greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or Null entries or Null.

Programmatic Pattern: ((RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | {(RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankCycleTimeLimit**

The maximum possible computed duration of all of the scans for the intact and fragmentation measurements when BlankAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Calculated from the BlankAcquisitionSurvey, BlankScanTime, and BlankFragmentScanTime.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 20000 seconds or list of one or more greater than or equal to 0.015 seconds and less than or equal to 20000 seconds or Null entries or Null.

Programmatic Pattern: ((RangeP\[0.015\*Second, 20000\*Second\] | {(RangeP\[0.015\*Second, 20000\*Second\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankExclusionDomain**

The time range when the BlankExclusionMasses are omitted in the chromatogram. Full indicates for the entire period.

Default Value: Automatic

Default Calculation: Set to the entire BlankAcquisitionWindow.

Pattern Description: A span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or Null entries or list of one or more list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full entries entries or Null.

Programmatic Pattern: (((GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full) | {(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full | Null)..} | {{(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full)..}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankExclusionMass**

The intact ions (Target Mass) to omit. When the Mode is set to All, the mass is excluded for the entire ExclusionDomain. When the Mode is set to Once, the Mass is excluded in the first survey appearance, but considered for consequent ones.

Default Value: Automatic

Default Calculation: If any BlankExclusionMode-related options are set (e.g. BlankExclusionMassTolerance), a target mass of the first Analyte (if not in BlankInclusionMasses) is chosen and retention time is set to 0\*Minute.

Pattern Description: List of one or more list of one or more {Mode, Target Mass} entries entries or list of one or more {Mode, Target Mass} or Null entries or {Mode, Target Mass} or Null.

Programmatic Pattern: (({All | Once, RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]} | {({All | Once, RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]} | Null)..} | {{{All | Once, RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]}..}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankExclusionMassTolerance**

The range above and below each ion in BlankExclusionMasses to consider for omission when BlankExclusionMass is All or Once.

Default Value: Automatic

Default Calculation: If BlankExclusionMass -> All or Once, set to 0.5 Gram/Mole; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | {(RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankExclusionRetentionTimeTolerance**

The range of time above and below the BlankExclusionDomain to consider for exclusion.

Default Value: Automatic

Default Calculation: If BlankExclusionMass and BlankExclusionDomain options are set, this is set to 10 seconds; otherwise, Null.

Pattern Description: Greater than or equal to 0 seconds and less than or equal to 3600 seconds or list of one or more greater than or equal to 0 seconds and less than or equal to 3600 seconds or Null entries or Null.

Programmatic Pattern: ((RangeP\[0\*Second, 3600\*Second\] | {(RangeP\[0\*Second, 3600\*Second\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankInclusionDomain**

The time range when BlankInclusionMass applies with respect to the chromatogram. Full indicates for the entire period.

Default Value: Automatic

Default Calculation: Set to the entire BlankAcquisitionWindow.

Pattern Description: A span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or Null entries or list of one or more list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full entries entries or Null.

Programmatic Pattern: (((GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full) | {(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full | Null)..} | {{(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full)..}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankInclusionMass**

The ions (Target Mass) to prioritize during the survey scan for further fragmentation when BlankAcquisitionMode is DataDependent. BlankInclusionMass set to Only will solely be considered for surveys. When Mode is Preferential, the InclusionMass will be prioritized for survey.

Default Value: Automatic

Default Calculation: When BlankInclusionMode Only or Preferential, an entry mass is added based on the mass of the most salient analyte of the sample.

Pattern Description: List of one or more list of one or more {Mode, Target Mass} entries entries or list of one or more {Mode, Target Mass} or Null entries or {Mode, Target Mass} or Null.

Programmatic Pattern: (({Only | Preferential, RangeP\[(2\*Gram)/Mole, (4000\*Gram)/Mole\]} | {({Only | Preferential, RangeP\[(2\*Gram)/Mole, (4000\*Gram)/Mole\]} | Null)..} | {{{Only | Preferential, RangeP\[(2\*Gram)/Mole, (4000\*Gram)/Mole\]}..}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankInclusionCollisionEnergy**

The overriding collision energy value that can be applied to the the BlankInclusionMass. Null will default to the BlankCollisionEnergy option and related.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0 volts and less than or equal to 255 volts or list of one or more greater than or equal to 0 volts and less than or equal to 255 volts or Null entries or list of one or more list of one or more greater than or equal to 0 volts and less than or equal to 255 volts entries entries or Null.

Programmatic Pattern: ((RangeP\[0\*Volt, 255\*Volt\] | {(RangeP\[0\*Volt, 255\*Volt\] | Null)..} | {{RangeP\[0\*Volt, 255\*Volt\]..}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankInclusionDeclusteringVoltage**

The overriding source voltage value that can be applied to the the BlankInclusionMass. Null will default to the BlankDeclusteringVoltage option.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 150 volts or list of one or more greater than or equal to 0.1 volts and less than or equal to 150 volts or Null entries or list of one or more list of one or more greater than or equal to 0.1 volts and less than or equal to 150 volts entries entries or Null.

Programmatic Pattern: ((RangeP\[0.1\*Volt, 150\*Volt\] | {(RangeP\[0.1\*Volt, 150\*Volt\] | Null)..} | {{RangeP\[0.1\*Volt, 150\*Volt\]..}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankInclusionChargeState**

The maximum charge state of the BlankInclusionMass to also consider for inclusion. For example, if this is set to 3 and the polarity is Positive, then +1,+2,+3 charge states will be considered as well.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0 and less than or equal to 6 in increments of 1 or list of one or more greater than or equal to 0 and less than or equal to 6 in increments of 1 or Null entries or list of one or more list of one or more greater than or equal to 0 and less than or equal to 6 in increments of 1 entries entries or Null.

Programmatic Pattern: ((RangeP\[0, 6, 1\] | {(RangeP\[0, 6, 1\] | Null)..} | {{RangeP\[0, 6, 1\]..}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankInclusionScanTime**

The overriding scan time duration that can be applied to the the BlankInclusionMass for the consequent fragmentation. Null will default to the BlankFragmentScanTime option.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 10 seconds or list of one or more greater than or equal to 0.015 seconds and less than or equal to 10 seconds or Null entries or list of one or more list of one or more greater than or equal to 0.015 seconds and less than or equal to 10 seconds entries entries or Null.

Programmatic Pattern: ((RangeP\[0.015\*Second, 10\*Second\] | {(RangeP\[0.015\*Second, 10\*Second\] | Null)..} | {{RangeP\[0.015\*Second, 10\*Second\]..}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankInclusionMassTolerance**

The range above and below each ion in BlankInclusionMass to consider for prioritization. For example, if set to 0.5 Gram/Mole, the total range is 1 Gram/Mole.

Default Value: Automatic

Default Calculation: Set to 0.5 Gram/Mole if BlankInclusionMass is given; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | {(RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankSurveyChargeStateExclusion**

Indicates if redundant ions that differ by ionic charge (+1/-1, +2/-2, etc.) should be left out and if BlankChargeState exclusion-related options should be automatically filled in.

Default Value: Automatic

Default Calculation: Set to True, if any of the BlankChargeState options are set; otherwise, False.

Pattern Description: List of one or more True or False or Null entries or True or False or Null.

Programmatic Pattern: ((BooleanP | {(BooleanP | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankSurveyIsotopeExclusion**

Indicates if redundant ions that differ by isotopic mass (e.g. 1, 2 Gram/Mole) should be excluded and if BlankMassIsotope exclusion-related options should be automatically filled in.

Default Value: Automatic

Default Calculation: Set to True, if any of the BlankIsotopeExclusion options are set; otherwise, False.

Pattern Description: List of one or more True or False or Null entries or True or False or Null.

Programmatic Pattern: ((BooleanP | {(BooleanP | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankChargeStateExclusionLimit**

The number of ions to survey first with exclusion by ionic state. For example, if BlankAcquisitionSurvey is 10 and this option is 5, then 5 ions will be surveyed with charge-state exclusion. For candidate ions of rank 6 to 10, no exclusion will be performed.

Default Value: Automatic

Default Calculation: Inherited from any supplied method; otherwise, set the same to BlankAcquisitionSurvey, if any ChargeState option is set.

Pattern Description: Greater than or equal to 0 and less than or equal to 30 in increments of 1 or list of one or more greater than or equal to 0 and less than or equal to 30 in increments of 1 or Null entries or Null.

Programmatic Pattern: ((RangeP\[0, 30, 1\] | {(RangeP\[0, 30, 1\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankChargeStateExclusion**

The specific ionic states of intact ions to redundantly exclude from the survey for further fragmentation/acquisition. 1 refers to +1/-1, 2 refers to +2/-2, etc.

Default Value: Automatic

Default Calculation: When BlankSurveyChargeStateExclusion is True, set to {1,2}; otherwise, Null.

Pattern Description: Greater than or equal to 1 and less than or equal to 6 in increments of 1 or list of one or more greater than or equal to 1 and less than or equal to 6 in increments of 1 or Null entries or Null.

Programmatic Pattern: ((RangeP\[1, 6, 1\] | {(RangeP\[1, 6, 1\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankChargeStateMassTolerance**

The range of m/z to consider for exclusion by ionic state property when BlankSurveyChargeStateExclusion is True.

Default Value: Automatic

Default Calculation: When BlankSurveyChargeStateExclusion is True, set to 0.5 Gram/Mole; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | {(RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankIsotopicExclusion**

The m/z difference between monoisotopic ions as a criterion for survey exclusion.

Default Value: Automatic

Default Calculation: When BlankSurveyIsotopeExclusion is True, set to 1 Gram/Mole; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null entries or list of one or more list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole entries entries or Null.

Programmatic Pattern: (((Alternatives\[RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\]\]) | {(RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Null)..} | {{(Alternatives\[RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\]\])..}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankIsotopeRatioThreshold**

The minimum relative magnitude between monoisotopic ions in order to be considered an isotope for exclusion.

Default Value: Automatic

Default Calculation: When BlankSurveyIsotopeExclusion is True, set to 0.1; otherwise, Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or list of one or more greater than or equal to 0 and less than or equal to 1 or Null entries or list of one or more list of one or more greater than or equal to 0 and less than or equal to 1 entries entries or Null.

Programmatic Pattern: ((RangeP\[0, 1\] | {(RangeP\[0, 1\] | Null)..} | {{RangeP\[0, 1\]..}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankIsotopeDetectionMinimum**

The acquisition rate of a given intact mass to consider for isotope exclusion in the survey.

Default Value: Automatic

Default Calculation: When BlankSurveyIsotopeExclusion is True, set to 10 1/Second; otherwise, Null.

Pattern Description: Greater than or equal to 0 reciprocal seconds or list of one or more greater than or equal to 0 reciprocal seconds or Null entries or list of one or more list of one or more greater than or equal to 0 reciprocal seconds entries entries or Null.

Programmatic Pattern: ((GreaterEqualP\[(0\*1)/Second\] | {(GreaterEqualP\[(0\*1)/Second\] | Null)..} | {{GreaterEqualP\[(0\*1)/Second\]..}..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankIsotopeMassTolerance**

The range of m/z around a mass to consider for exclusion. This applies for both ChargeState and mass shifted Isotope. If set to 0.5 Gram/Mole, then the total range should be 1 Gram/Mole.

Default Value: Automatic

Default Calculation: When BlankSurveyIsotopeExclusion or BlankSurveyChargeStateExclusion is True, set to 0.5 Gram/Mole; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | {(RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankIsotopeRatioTolerance**

The range of relative magnitude around BlankIsotopeRatio to consider for isotope exclusion.

Default Value: Automatic

Default Calculation: If BlankSurveyIsotopeExclusion is True, set to 30\*Percent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more greater than or equal to 0 percent and less than or equal to 100 percent or Null entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {(RangeP\[0\*Percent, 100\*Percent\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankNeutralLoss**

A neutral loss scan is performed on ESI-QQQ mass spectrometry by scanning the sample through the first quadrupole (Q1). The ions are then fragmented in the collision cell. The second mass analyzer is then scanned with a fixed offset to MS1. This option represents the value of this offset.

Default Value: Automatic

Default Calculation: Is set to 500 g/mol if using NeutralIonLoss as the BlankAcquisitionMode, and is Null in other modes.

Pattern Description: Greater than 0 grams per mole or list of one or more greater than 0 grams per mole or Null entries or Null.

Programmatic Pattern: ((GreaterP\[(0\*Gram)/Mole\] | {(GreaterP\[(0\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankDwellTime**

The duration of time for which spectra are acquired at the specific mass detection value for SelectedIonMonitoring and MultipleReactionMonitoring mode in ESI-QQQ.

Default Value: Automatic

Default Calculation: Is automatically set to 200 microsecond if BlankAcquisition is in SelectedIonMonitoring or MultipleReactionMonitoring mode.

Pattern Description: Greater than or equal to 5 milliseconds and less than or equal to 2000 milliseconds or list of one or more greater than or equal to 5 milliseconds and less than or equal to 2000 milliseconds or Null entries or Null.

Programmatic Pattern: ((RangeP\[5\*Millisecond, 2000\*Millisecond\] | {(RangeP\[5\*Millisecond, 2000\*Millisecond\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankCollisionCellExitVoltage**

Also known as the Collision Cell Exit Potential (CXP). This value focuses and accelerates the ions out of collision cell (Q2) and into 2nd mass analyzer (MS 2). This potential is tuned to ensure successful ion acceleration out of collision cell and into MS2, and can be adjusted to reach the maximal signal intensity. This option is unique to ESI-QQQ for now, and only required when Fragment ->True and/or in ScanMode that achieves tandem mass feature (PrecursorIonScan, NeutralIonLoss,ProductIonScan,MultipleReactionMonitoring). For non-tandem mass ScanMode (FullScan and SelectedIonMonitoring) and other massspectrometer (ESI-QTOF and MALDI-TOF), this option is resolved to Null.

Default Value: Automatic

Default Calculation: For TripleQuandrupole as the MassAnalyzer, is set to first CollisionCellExitVoltage, otherwise set to Null.

Pattern Description: Greater than or equal to -55 volts and less than or equal to 55 volts or list of one or more greater than or equal to -55 volts and less than or equal to 55 volts or Null entries or Null.

Programmatic Pattern: ((RangeP\[-55\*Volt, 55\*Volt\] | {(RangeP\[-55\*Volt, 55\*Volt\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankMassDetectionStepSize**

Indicate the step size for mass collection in range when using TripleQuadruploe as the MassAnalyzer.

Default Value: Automatic

Default Calculation: This option will be set to Null if using ESI-QTOF. For ESI-QQQ, if both of the mass anaylzer are in mass selection mode (SelectedIonMonitoring and MultipleReactionMonitoring mode), this option will be auto resolved to Null. In all other mass scan modes in ESI-QQQ, this option will be automatically resolved to 0.1 g/mol.

Pattern Description: Greater than or equal to 0.01 grams per mole and less than or equal to 1 gram per mole or list of one or more greater than or equal to 0.01 grams per mole and less than or equal to 1 gram per mole or Null entries or Null.

Programmatic Pattern: ((RangeP\[(0.01\*Gram)/Mole, (1\*Gram)/Mole\] | {(RangeP\[(0.01\*Gram)/Mole, (1\*Gram)/Mole\] | Null)..}) | Automatic) | Null

Index Matches to: Blank

#### **BlankMultipleReactionMonitoringAssays**

In ESI-QQQ mass spectrometry analysis, the ion corresponding to the compound of interest is targetted with subsequent fragmentation of that target ion to produce a range of daughter ions. One (or more) of these fragment daughter ions can be selected for quantitation purposes. Only compounds that meet both these criteria, i.e. specific parent ion and specific daughter ions corresponding to the mass of the molecule of interest are detected within the mass spectrometer. The mass assays (MS1/MS2 mass value combinations) for each scan, along with the CollisionEnergy and DwellTime (length of time of each scan).

Default Value: Automatic

Default Calculation: Is set based one BlankMassDetection, BlankCollissionEnergy, BlankDwellTime and BlankFramentMassDetection.

Pattern Description: List of one or more list of one or more Individual Multiple Reaction Monitoring Assay or None entries or Null entries or Null or Null.

Programmatic Pattern: (({({({GreaterP\[(0\*Gram)/Mole\], (RangeP\[5\*Volt, 180\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\]) | Automatic, GreaterP\[(0\*Gram)/Mole\], GreaterP\[0\*Second\] | Automatic} | Null)..} | Null)..} | Null) | Automatic) | Null

Index Matches to: Blank

#### **BlankAbsorbanceWavelength**

The physical properties of light passed through the flow for the PhotoDiodeArray (PDA) Detector for Blank measurement.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in AbsorbanceWavelength.

Pattern Description: All or Range or Single or Null.

Programmatic Pattern: ((RangeP\[190\*Nanometer, 500\*Nanometer, 1\*Nanometer\] | All | RangeP\[190\*Nanometer, 490\*Nanometer, 1\*Nanometer\] ;; RangeP\[200\*Nanometer, 500\*Nanometer, 1\*Nanometer\]) | Automatic) | Null

Index Matches to: Blank

#### **BlankWavelengthResolution**

The increment of wavelength for the range of light passed through the flow for absorbance measurement with the photo diode array (PDA) detector during Blank measurement.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in WavelengthResolution.

Pattern Description: Greater than or equal to 1.2 nanometers and less than or equal to 12. nanometers or Null.

Programmatic Pattern: (RangeP\[1.2\*Nanometer, 12.\*Nanometer\] | Automatic) | Null

Index Matches to: Blank

#### **BlankUVFilter**

Indicates if UV wavelengths (less than 210 nm) should be blocked from being transmitted through the Blank for the PhotoDiodeArray (PDA) detector.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in UVFilter.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: Blank

#### **BlankAbsorbanceSamplingRate**

The frequency of Blank measurement. Lower values will be less susceptible to noise but will record less frequently across time.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in AbsorbanceSamplingRate.

Pattern Description: Greater than or equal to 1 reciprocal second and less than or equal to 80 reciprocal seconds in increments of 1 reciprocal second or Null.

Programmatic Pattern: (RangeP\[(1\*1)/Second, (80\*1)/Second, (1\*1)/Second\] | Automatic) | Null

Index Matches to: Blank

#### **BlankStorageCondition**

The non-default conditions under which any blanks used by this experiment should be stored after the protocol is completed. If left unset, the blank samples will be stored according to their Models' DefaultStorageCondition.

Default Value: Null

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, BacteriaIncubation, MammalianIncubation, TissueCultureCellsIncubation, MicrobialCellsIncubation, MicrobialCellsShakingIncubation, YeastCellsIncubation, YeastCellsShakingIncubation, ViralIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: (Alternatives\[SampleStorageTypeP | Disposal\]) | Null

Index Matches to: Blank

### ColumnPrime

#### **ColumnRefreshFrequency**

The frequency at which column flushes (where solvent is flowed without injection in order to release adsorbed compounds within the column) and primes (where solvent is flowed in order to equilibrate the column) will be inserted into the order of analyte injections. An initial column prime and final column flush will be performed unless Null or None is specified.

Default Value: Automatic

Default Calculation: Set to Null when InjectionTable option is specified (meaning that this option is inconsequential); otherwise, set to FirstAndLast (meaning initial column prime before the measurements and final column flush after measurements.) when there is a Column. Set to None if there is no Column (meaning no column flush).

Pattern Description: Greater than 0 in increments of 1 or None or FirstAndLast or Null.

Programmatic Pattern: (((None | FirstAndLast) | GreaterP\[0, 1\]) | Automatic) | Null

#### **ColumnPrimeTemperature**

The column's temperature at which the column prime gradient is run.

Default Value: Automatic

Default Calculation: Automatically set from ColumnTemperature. Automatic resolution can be inherited from the ColumnPrimeGradient option.

Pattern Description: Ambient or greater than or equal to 5 degrees Celsius and less than or equal to 80 degrees Celsius or Null.

Programmatic Pattern: ((RangeP\[5\*Celsius, 80\*Celsius\] | Ambient) | Automatic) | Null

#### **ColumnPrimeGradientA**

The composition of BufferA within the flow, defined for specific time points for column prime.

Default Value: Automatic

Default Calculation: Automatically set from ColumnPrimeGradient option or implicitly resolved from ColumnPrimeGradientB, ColumnPrimeGradientC, and ColumnPrimeGradientD options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer A Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

#### **ColumnPrimeGradientB**

The composition of BufferB within the flow, defined for specific time points for column prime.

Default Value: Automatic

Default Calculation: Automatically set from ColumnPrimeGradient option or implicitly resolved from ColumnPrimeGradientA, ColumnPrimeGradientC, and ColumnPrimeGradientD options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer B Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

#### **ColumnPrimeGradientC**

The composition of BufferC within the flow, defined for specific time points for column prime.

Default Value: Automatic

Default Calculation: Automatically set from ColumnPrimeGradient option or implicitly resolved from ColumnPrimeGradientA, ColumnPrimeGradientB, and ColumnPrimeGradientD options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer C Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

#### **ColumnPrimeGradientD**

The composition of BufferD within the flow, defined for specific time points for column prime.

Default Value: Automatic

Default Calculation: Automatically set from ColumnPrimeGradient option or implicitly resolved from ColumnPrimeGradientA, ColumnPrimeGradientB, and ColumnPrimeGradientC options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer D Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

#### **ColumnPrimeFlowRate**

The speed of the fluid through the system for column prime.

Default Value: Automatic

Default Calculation: Automatically set from Type and Scale or inherited from the method given in the ColumnPrimeGradient option.

Pattern Description: Greater than or equal to 0 milliliters per minute and less than or equal to 2 milliliters per minute or list of one or more {Time, Flow Rate} entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Milliliter)/Minute, (2\*Milliliter)/Minute\] | {{GreaterEqualP\[0\*Minute\], RangeP\[(0\*Milliliter)/Minute, (2\*Milliliter)/Minute\]}..}) | Automatic) | Null

#### **ColumnPrimeStart**

A shorthand option to specify the starting BufferB composition for column prime runs. This option must be specified with ColumnPrimeEnd and ColumnPrimeDuration.

Default Value: Null

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or Null.

Programmatic Pattern: RangeP\[0\*Percent, 100\*Percent\] | Null

#### **ColumnPrimeEnd**

A shorthand option to specify the final BufferB composition for column prime runs. This option must be specified with ColumnPrimeStart and ColumnPrimeDuration.

Default Value: Null

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or Null.

Programmatic Pattern: RangeP\[0\*Percent, 100\*Percent\] | Null

#### **ColumnPrimeDuration**

A shorthand option to specify the duration of the column prime gradient.

Default Value: Null

Pattern Description: Greater than or equal to 0 minutes or Null.

Programmatic Pattern: GreaterEqualP\[0\*Minute\] | Null

#### **ColumnPrimeGradient**

The buffer composition over time in the fluid flow for column prime.

Default Value: Automatic

Default Calculation: Automatically set to best meet all the ColumnPrimeGradient\_ options (e.g. ColumnPrimeGradientA, ColumnPrimeGradientB, ColumnPrimeGradientC, ColumnPrimeGradientD, ColumnPrimeDuration).

Pattern Description: An object of type or subtype Object\[Method, Gradient\] or list of one or more {Time, Buffer A Composition, Buffer B Composition, Buffer C Composition, Buffer D Composition, Flow Rate} entries or Null.

Programmatic Pattern: ((ObjectP\[Object\[Method, Gradient\]\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[(0\*Milliliter)/Minute, (2\*Milliliter)/Minute\]}..}) | Automatic) | Null

#### **ColumnPrimeIonMode**

Indicates if positively or negatively charged ions are analyzed.

Default Value: Automatic

Default Calculation: Set to the first IonMode for an analyte input sample.

Pattern Description: Negative or Positive or Null.

Programmatic Pattern: (IonModeP | Automatic) | Null

#### **ColumnPrimeMassSpectrometryMethod**

The previously specified instruction(s) for the analyte ionization, selection, fragmentation, and detection.

Default Value: Automatic

Default Calculation: If ColumnPrime samples exist and MassSpectrometryMethod is specified, then set to the first available ColumnPrimeMassSpectrometryMethod.

Pattern Description: An object of type or subtype Object\[Method, MassAcquisition\] or New or Null.

Programmatic Pattern: ((ObjectP\[Object\[Method, MassAcquisition\]\] | New) | Automatic) | Null

#### **ColumnPrimeESICapillaryVoltage**

The absolute voltage applied to the tip of the stainless steel capillary tubing in order to produce charged droplets. Adjust this voltage to maximize sensitivity. Most compounds are optimized between 0.5 and 3.2 kV in ESI positive ion mode and 0.5 and 2.6 in ESI negative ion mode, but can be altered according to sample type. For low flow applications, best sensitivity will be achieved with a relatively high value in ESI positive (e.g. 3.0 kV), for columnPrime flow UPLC a value of 0.5 kV is typically best for maximum sensitivity.

Default Value: Automatic

Default Calculation: Is automatically set to the first ESICapillaryVoltage.

Pattern Description: Greater than or equal to -4 kilovolts and less than or equal to 5 kilovolts or Null.

Programmatic Pattern: (RangeP\[-4\*Kilovolt, 5\*Kilovolt\] | Automatic) | Null

#### **ColumnPrimeDeclusteringVoltage**

The voltage offset between the ion block (the reduced pressure chamber of the source block) and the stepwave ion guide (the optics before the quadrupole mass analyzer). This voltage attracts charged ions in the spray being produced from the capillary tip into the ion block leading into the mass spectrometer. This voltage is typically set to 25-100 V and its tuning has little effect on sensitivity compared to other options (e.g. ColumnPrimeStepwaveVoltage).

Default Value: Automatic

Default Calculation: Is automatically set to any specified MassAcquisition method; otherwise, set to 40 Volt.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 150 volts or Null.

Programmatic Pattern: (RangeP\[0.1\*Volt, 150\*Volt\] | Automatic) | Null

#### **ColumnPrimeStepwaveVoltage**

The voltage offset between the 1st and 2nd stage of the stepwave ion guide which leads ions coming from the sample cone towards the quadrupole mass analyzer. This voltage normally optimizes between 25 and 150 V and should be adjusted for sensitivity depending on compound and charge state. For multiply charged species it is typically set to to 40-50 V, and higher for singly charged species. In general higher cone voltages (120-150 V) are needed for larger mass ions such as intact proteins and monoclonal antibodies. It also has greatest effect on in-source fragmentation and should be decreased if in-source fragmentation is observed but not desired.

Default Value: Automatic

Default Calculation: Is automatically set to the first StepwaveVoltage.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 200 volts or Null.

Programmatic Pattern: (RangeP\[0.1\*Volt, 200\*Volt\] | Automatic) | Null

#### **ColumnPrimeSourceTemperature**

The temperature setting of the source block. Heating the source block discourages condensation and decreases solvent clustering in the reduced vacuum region of the source. This temperature setting is flow rate and sample dependent. Typical values are between 60 to 120 Celsius. For thermally labile analytes, a lower temperature setting is recommended.

Default Value: Automatic

Default Calculation: Is automatically set to the first SourceTemperature.

Pattern Description: Greater than or equal to 25 degrees Celsius and less than or equal to 150 degrees Celsius or Null.

Programmatic Pattern: (RangeP\[25\*Celsius, 150\*Celsius\] | Automatic) | Null

#### **ColumnPrimeDesolvationTemperature**

The temperature setting for the ESI desolvation heater that controls the nitrogen gas temperature used for solvent evaporation to produce single gas phase ions from the ion spray. Similar to ColumnPrimeDesolvationGasFlow, this setting is dependent on solvent flow rate and composition. A typical range is from 150 to 650 Celsius.

Default Value: Automatic

Default Calculation: Is automatically set to the first DesolvationTemperature.

Pattern Description: Greater than or equal to 20 degrees Celsius and less than or equal to 650 degrees Celsius or Null.

Programmatic Pattern: (RangeP\[20\*Celsius, 650\*Celsius\] | Automatic) | Null

#### **ColumnPrimeDesolvationGasFlow**

The rate at which nitrogen gas is flowed around the ESI capillary. It is used for solvent evaporation to produce single gas phase ions from the ion spray. Similar to ColumnPrimeDesolvationTemperature, this setting is dependent on solvent flow rate and composition. Higher desolvation temperatures usually result in increased sensitivity, but too high values can cause spray instability. Typical values are between 300 to 1200 L/h.

Default Value: Automatic

Default Calculation: Is automatically set to the first DesolvationGasFlow.

Pattern Description: Greater than or equal to 55 liters per hour and less than or equal to 1200 liters per hour or greater than or equal to 0 pounds‐force per inch squared and less than or equal to 85 pounds‐force per inch squared or Null.

Programmatic Pattern: ((RangeP\[(55\*Liter)/Hour, (1200\*Liter)/Hour\] | RangeP\[0\*PSI, 85\*PSI\]) | Automatic) | Null

#### **ColumnPrimeConeGasFlow**

The rate at which nitrogen gas flow is flowed around the sample inlet cone (the spherical metal plate acting as a first gate between the sprayer and the reduced pressure chamber, the ion block). This gas flow is used to minimize the formation of solvent ion clusters. It also helps reduce adduct ions and directing the spray into the ion block while keeping the sample cone clean. Typical values are between 0 and 150 L/h.

Default Value: Automatic

Default Calculation: Is automatically set to the first ConeGasFlow.

Pattern Description: Greater than or equal to 0 liters per hour and less than or equal to 300 liters per hour or greater than or equal to 30 pounds‐force per inch squared and less than or equal to 55 pounds‐force per inch squared or Null.

Programmatic Pattern: ((RangeP\[(0\*Liter)/Hour, (300\*Liter)/Hour\] | RangeP\[30\*PSI, 55\*PSI\]) | Automatic) | Null

#### **ColumnPrimeAcquisitionWindow**

The time range with respect to the the chromatographic separation to conduct analyte ionization, selection/survey, optional fragmentation, and detection.

Default Value: Automatic

Default Calculation: Set to the entire gradient window 0 Minute to the last time point in ColumnPrimeGradient.

Pattern Description: A span from anything greater than or equal to 0 minutes and less than or equal to 8 hours to anything greater than or equal to 0 minutes and less than or equal to 8 hours or Null.

Programmatic Pattern: (RangeP\[0\*Minute, 8\*Hour\] ;; RangeP\[0\*Minute, 8\*Hour\] | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeAcquisitionMode**

The method by which spectra are collected. DataDependent will depend on the properties of the measured mass spectrum of the intact ions. DataIndependent will systemically scan through all of the intact ions. MS1FullScan will focus on defined intact masses. MS1MS2 will focus on fragmented masses.

Default Value: Automatic

Default Calculation: Set to MS1FullScan unless DataDependent related options are set, then set to DataDependent.

Pattern Description: DataIndependent, DataDependent, MS1FullScan, MS1MS2ProductIonScan, SelectedIonMonitoring, NeutralIonLoss, PrecursorIonScan, or MultipleReactionMonitoring or Null.

Programmatic Pattern: (MSAcquisitionModeP | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeFragment**

Indicates if ions should be collided with neutral gas in order to measure the resulting product ions. Also known as tandem mass spectrometry or MS/MS (as opposed to MS).

Default Value: Automatic

Default Calculation: Set to True if ColumnPrimeAcquisitionMode is MS1MS2ProductIonScan, DataDependent, or DataIndependent. Set True if any of the Fragmentation related options are set (e.g. ColumnPrimeFragmentMassDetection).

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeMassDetection**

The lowest and the highest mass-to-charge ratio (m/z) to be recorded or selected for intact masses. When ColumnPrimeFragment is True, the intact ions will be selected for fragmentation.

Default Value: Automatic

Default Calculation: For ColumnPrimeFragment -> False, automatically set to one of three default mass ranges according to the molecular weight of the ColumnPrimeAnalytes to encompass them.

Pattern Description: All or Range or Single or Specific List or Null.

Programmatic Pattern: ((RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | {RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]..} | RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] ;; RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | MSAnalyteGroupP) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeScanTime**

The duration of time allowed to pass between each spectral acquisition. When ColumnPrimeAcquisitionMode is DataDependent, this value refers to the duration for measuring spectra from the intact ions. Increasing this value improves sensitivity whereas decreasing this value allows for more data points and spectra to be acquired.

Default Value: Automatic

Default Calculation: Set to 0.2 seconds unless a method is given.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 10 seconds.

Programmatic Pattern: RangeP\[0.015\*Second, 10\*Second\] | Automatic

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeFragmentMassDetection**

The lowest and the highest mass-to-charge ratio (m/z) to be recorded or selected for product ions. When ColumnPrimeAcquisitionMode is DataDependent|DataIndependent, all of the product ions in consideration for measurement. Null if ColumnPrimeFragment is False.

Default Value: Automatic

Default Calculation: When ColumnPrimeFragment is False, set to Null. Otherwise, 20 Gram/Mole to the maximum ColumnPrimeMassDetection.

Pattern Description: All or Range or Specific or Null.

Programmatic Pattern: (({RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\]..} | All | RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\] ;; RangeP\[(100\*Gram)/Mole, (16000\*Gram)/Mole\]) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeCollisionEnergy**

The voltage by which intact ions are accelerated through inert gas in order to dissociate them into measurable fragment ion species when ColumnPrimeFragment is True. ColumnPrimeCollisionEnergy cannot be defined simultaneously with ColumnPrimeCollisionEnergyMassProfile.

Default Value: Automatic

Default Calculation: Is automatically set to 40 Volt when ColumnPrimeFragment is True, otherwise is set to Null.

Pattern Description: Greater than or equal to 5 volts and less than or equal to 255 volts or greater than or equal to -180 volts and less than or equal to 5 volts or list of one or more greater than or equal to 5 volts and less than or equal to 180 volts or greater than or equal to -180 volts and less than or equal to 5 volts entries or Null.

Programmatic Pattern: (((RangeP\[5\*Volt, 255\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\]) | {(RangeP\[5\*Volt, 180\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\])..}) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeCollisionEnergyMassProfile**

The relationship of collision energy with the ColumnPrimeMassDetection.

Default Value: Automatic

Default Calculation: Set to ColumnPrimeCollisionEnergyMassScan if defined; otherwise, set to Null.

Pattern Description: A span from anything greater than or equal to 0.1 volts and less than or equal to 255 volts to anything greater than or equal to 0.1 volts and less than or equal to 255 volts or Null.

Programmatic Pattern: (RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\] | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeCollisionEnergyMassScan**

The collision energy profile at the end of the scan from ColumnPrimeCollisionEnergy or ColumnPrimeCollisionEnergyScanProfile, as related to analyte mass.

Default Value: Automatic

Pattern Description: Constant or Range or Null.

Programmatic Pattern: ((RangeP\[0.1\*Volt, 255\*Volt\] | RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\]) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeFragmentScanTime**

The duration of the spectral scanning for each fragmentation of an intact ion when ColumnPrimeAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Automatically set to the same value as ScanTime if ColumnPrimeAcquisitionMode is DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 10 seconds or Null.

Programmatic Pattern: ((Alternatives\[RangeP\[0.015\*Second, 10\*Second\]\]) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeAcquisitionSurvey**

The number of intact ions to consider for fragmentation and product ion measurement in every measurement cycle when ColumnPrimeAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Automatically set to 10 if ColumnPrimeAcquisitionMode is set to DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 1 and less than or equal to 30 in increments of 1 or Null.

Programmatic Pattern: (RangeP\[1, 30, 1\] | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeMinimumThreshold**

The minimum number of total ions detected within ScanTime durations needed to trigger the start of data dependent acquisition when ColumnPrimeAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Automatically set to (100000/Second)\*ScanTime if ColumnPrimeAcquisitionMode is DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or Null.

Programmatic Pattern: (RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeAcquisitionLimit**

The maximum number of total ions for a specific intact ion when ColumnPrimeAcquisitionMode is set to DataDependent. When this value is exceeded, acquisition will switch to fragmentation of the next candidate ion.

Default Value: Automatic

Default Calculation: Automatically inherited from supplied method if ColumnPrimeAcquisitionMode is set to DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or Null.

Programmatic Pattern: (RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeCycleTimeLimit**

The maximum possible computed duration of all of the scans for the intact and fragmentation measurements when ColumnPrimeAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Calculated from the ColumnPrimeAcquisitionSurvey, ColumnPrimeScanTime, and ColumnPrimeFragmentScanTime.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 20000 seconds or Null.

Programmatic Pattern: (RangeP\[0.015\*Second, 20000\*Second\] | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeExclusionDomain**

THe time range when the ColumnPrimeExclusionMasses are omitted in the chromatogram. Full indicates for the entire period.

Default Value: Automatic

Default Calculation: Set to the entire ColumnPrimeAcquisitionWindow.

Pattern Description: A span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full entries or Null.

Programmatic Pattern: (((GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full) | {(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full)..}) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeExclusionMass**

The intact ions (Target Mass) to omit. When the Mode is set to All, the mass is excluded for the entire ExclusionDomain. When set to Once, the mass is excluded in the first survey appearance, but considered for consequent ones.

Default Value: Automatic

Default Calculation: If any ColumnPrimeExclusionMode-related options are set (e.g. ColumnPrimeExclusionMassTolerance), a target mass of the first Analyte (if not in ColumnPrimeInclusionMasses) is chosen and retention time is set to 0\*Minute.

Pattern Description: List of one or more {Mode, Target Mass} entries or {Mode, Target Mass} or Null.

Programmatic Pattern: (({All | Once, RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]} | {{All | Once, RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]}..}) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeExclusionMassTolerance**

The range above and below each ion in ColumnPrimeExclusionMasses to consider for omission when ColumnPrimeExclusionMass is set to All or Once.

Default Value: Automatic

Default Calculation: If ColumnPrimeExclusionMass -> All or Once, set to 0.5 Gram/Mole; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null.

Programmatic Pattern: (RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeExclusionRetentionTimeTolerance**

The range of time above and below the ColumnPrimeExclusionDomain to consider for exclusion.

Default Value: Automatic

Default Calculation: If ColumnPrimeExclusionMass and ColumnPrimeExclusionDomain options are set, this is set to 10 seconds; otherwise, Null.

Pattern Description: Greater than or equal to 0 seconds and less than or equal to 3600 seconds or Null.

Programmatic Pattern: (RangeP\[0\*Second, 3600\*Second\] | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeInclusionDomain**

The time range when the ColumnPrimeInclusionMass applies with respect to the chromatogram. Full indicates for the entire period.

Default Value: Automatic

Default Calculation: Set to the entire ColumnPrimeAcquisitionWindow.

Pattern Description: A span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full entries or Null.

Programmatic Pattern: (((GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full) | {(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full)..}) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeInclusionMass**

The ions (Target Mass) to prioritize during the survey scan for further fragmentation when ColumnPrimeAcquisitionMode is DataDependent. ColumnPrimeInclusionMass set to Only will solely be considered for surveys. When Mode is Preferential, the InclusionMass will be prioritized for survey.

Default Value: Automatic

Default Calculation: When ColumnPrimeInclusionMode Only or Preferential, an entry mass is added based on the mass of the most salient analyte of the sample.

Pattern Description: List of one or more {Mode, Target Mass} entries or {Mode, Target Mass} or Null.

Programmatic Pattern: (({Only | Preferential, RangeP\[(2\*Gram)/Mole, (4000\*Gram)/Mole\]} | {{Only | Preferential, RangeP\[(2\*Gram)/Mole, (4000\*Gram)/Mole\]}..}) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeInclusionCollisionEnergy**

The overriding collision energy value that can be applied to the the ColumnPrimeInclusionMass. Null will default to the ColumnPrimeCollisionEnergy option and related.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0 volts and less than or equal to 255 volts or list of one or more greater than or equal to 0 volts and less than or equal to 255 volts entries or Null.

Programmatic Pattern: ((RangeP\[0\*Volt, 255\*Volt\] | {RangeP\[0\*Volt, 255\*Volt\]..}) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeInclusionDeclusteringVoltage**

The overriding source voltage value that can be applied to the the ColumnPrimeInclusionMass. Null will default to the ColumnPrimeDeclusteringVoltage option.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 150 volts or list of one or more greater than or equal to 0.1 volts and less than or equal to 150 volts entries or Null.

Programmatic Pattern: ((RangeP\[0.1\*Volt, 150\*Volt\] | {RangeP\[0.1\*Volt, 150\*Volt\]..}) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeInclusionChargeState**

The maximum charge state of the ColumnPrimeInclusionMass to also consider for inclusion. For example, if this is set to 3 and the polarity is Positive, then +1,+2,+3 charge states will be considered as well.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0 and less than or equal to 6 in increments of 1 or list of one or more greater than or equal to 0 and less than or equal to 6 in increments of 1 entries or Null.

Programmatic Pattern: ((RangeP\[0, 6, 1\] | {RangeP\[0, 6, 1\]..}) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeInclusionScanTime**

The overriding scan time duration that can be applied to the the ColumnPrimeInclusionMass for the consequent fragmentation. Null will default to the ColumnPrimeFragmentScanTime option.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 10 seconds or list of one or more greater than or equal to 0.015 seconds and less than or equal to 10 seconds entries or Null.

Programmatic Pattern: ((RangeP\[0.015\*Second, 10\*Second\] | {RangeP\[0.015\*Second, 10\*Second\]..}) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeInclusionMassTolerance**

The range above and below each ion in ColumnPrimeInclusionMass to consider for prioritization. For example, if set to 0.5 Gram/Mole, the total range is 1 Gram/Mole.

Default Value: Automatic

Default Calculation: Set to 0.5 Gram/Mole if ColumnPrimeInclusionMass is given; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null.

Programmatic Pattern: ((Alternatives\[RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\]\]) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeSurveyChargeStateExclusion**

Indicates if redundant ions that differ by ionic charge (+1/-1, +2/-2, etc.) should be excluded and if ColumnPrimeChargeState exclusion-related options should be automatically filled in.

Default Value: Automatic

Default Calculation: Set to True, if any of the ColumnPrimeChargeState options are set; otherwise, False.

Pattern Description: True or False or Null.

Programmatic Pattern: ((Alternatives\[BooleanP\]) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeSurveyIsotopeExclusion**

Indicates if redundant ions that differ by isotopic mass (e.g. 1, 2 Gram/Mole) should be excluded and if ColumnPrimeMassIsotope exclusion-related options should be automatically filled in.

Default Value: Automatic

Default Calculation: Set to True, if any of the ColumnPrimeIsotopeExclusion options are set; otherwise, False.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeChargeStateExclusionLimit**

The number of ions to survey first with exclusion by ionic state. For example, if ColumnPrimeAcquisitionSurvey is 10 and this option is 5, then 5 ions will be surveyed with charge-state exclusion. For candidate ions of rank 6 to 10, no exclusion will be performed.

Default Value: Automatic

Default Calculation: Inherited from any supplied method; otherwise, set the same to ColumnPrimeAcquisitionSurvey, if any ChargeState option is set.

Pattern Description: Greater than or equal to 0 and less than or equal to 30 in increments of 1 or Null.

Programmatic Pattern: (RangeP\[0, 30, 1\] | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeChargeStateExclusion**

The specific ionic states of intact ions to redundantly exclude from the survey for further fragmentation/acquisition. 1 refers to +1/-1, 2 refers to +2/-2, etc.

Default Value: Automatic

Default Calculation: When ColumnPrimeSurveyChargeStateExclusion is True, set to {1,2}; otherwise, Null.

Pattern Description: Greater than or equal to 1 and less than or equal to 6 in increments of 1 or list of one or more greater than or equal to 1 and less than or equal to 6 in increments of 1 entries or Null.

Programmatic Pattern: ((RangeP\[1, 6, 1\] | {RangeP\[1, 6, 1\]..}) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeChargeStateMassTolerance**

The range of m/z to consider for exclusion by ionic state property when ColumnPrimeSurveyChargeStateExclusion is True.

Default Value: Automatic

Default Calculation: When ColumnPrimeSurveyChargeStateExclusion is True, set to 0.5 Gram/Mole; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null.

Programmatic Pattern: (RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeIsotopicExclusion**

The m/z difference between monoisotopic ions as a criterion for survey exclusion.

Default Value: Automatic

Default Calculation: When ColumnPrimeSurveyIsotopeExclusion is True, set to 1 Gram/Mole; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole entries or Null.

Programmatic Pattern: (((Alternatives\[RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\]\]) | {(Alternatives\[RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\]\])..}) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeIsotopeRatioThreshold**

The minimum relative magnitude between monoisotopic ions in order to be considered an isotope for exclusion.

Default Value: Automatic

Default Calculation: When ColumnPrimeSurveyIsotopeExclusion is True, set to 0.1; otherwise, Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or list of one or more greater than or equal to 0 and less than or equal to 1 entries or Null.

Programmatic Pattern: ((RangeP\[0, 1\] | {RangeP\[0, 1\]..}) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeIsotopeDetectionMinimum**

The acquisition rate of a given intact mass to consider for isotope exclusion in the survey.

Default Value: Automatic

Default Calculation: When ColumnPrimeSurveyIsotopeExclusion is True, set to 10 1/Second; otherwise, Null.

Pattern Description: Greater than or equal to 0 reciprocal seconds or list of one or more greater than or equal to 0 reciprocal seconds entries or Null.

Programmatic Pattern: ((GreaterEqualP\[(0\*1)/Second\] | {GreaterEqualP\[(0\*1)/Second\]..}) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeIsotopeMassTolerance**

The range of m/z around a mass to consider for exclusion. This applies for both ChargeState and mass shifted Isotope. If set to 0.5 Gram/Mole, then the total range should be 1 Gram/Mole.

Default Value: Automatic

Default Calculation: When ColumnPrimeSurveyIsotopeExclusion or ColumnPrimeSurveyChargeStateExclusion is True, set to 0.5 Gram/Mole; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null.

Programmatic Pattern: ((Alternatives\[RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\]\]) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeIsotopeRatioTolerance**

The range of relative magnitude around ColumnPrimeIsotopeRatio to consider for isotope exclusion.

Default Value: Automatic

Default Calculation: If ColumnPrimeSurveyIsotopeExclusion is True, set to 30\*Percent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or Null.

Programmatic Pattern: ((Alternatives\[RangeP\[0\*Percent, 100\*Percent\]\]) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeNeutralLoss**

A neutral loss scan is performed on ESI-QQQ mass spectrometry by scanning the sample through the first quadrupole (Q1). The ions are then fragmented in the collision cell. The second mass analyzer is then scanned with a fixed offset to MS1. This option represents the value of this offset.

Default Value: Automatic

Default Calculation: Is set to 500 g/mol if using NeutralIonLoss as the ColumnPrimeAcquisitionMode, and is Null in other modes.

Pattern Description: Greater than 0 grams per mole or Null.

Programmatic Pattern: (GreaterP\[(0\*Gram)/Mole\] | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeDwellTime**

The duration of time for which spectra are acquired at the specific mass detection value for SelectedIonMonitoring and MultipleReactionMonitoring mode in ESI-QQQ.

Default Value: Automatic

Default Calculation: Is automatically set to 200 microsecond if ColumnPrimeAcquisitionMode is in SelectedIonMonitoring or MultipleReactionMonitoring mode.

Pattern Description: Greater than or equal to 5 milliseconds and less than or equal to 2000 milliseconds or list of one or more greater than or equal to 5 milliseconds and less than or equal to 2000 milliseconds entries or Null.

Programmatic Pattern: ((RangeP\[5\*Millisecond, 2000\*Millisecond\] | {RangeP\[5\*Millisecond, 2000\*Millisecond\]..}) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeCollisionCellExitVoltage**

Also known as the Collision Cell Exit Potential (CXP). This value focuses and accelerates the ions out of collision cell (Q2) and into 2nd mass analyzer (MS 2). This potential is tuned to ensure successful ion acceleration out of collision cell and into MS2, and can be adjusted to reach the maximal signal intensity. This option is unique to ESI-QQQ for now, and only required when Fragment ->True and/or in ScanMode that achieves tandem mass feature (PrecursorIonScan, NeutralIonLoss,ProductIonScan,MultipleReactionMonitoring). For non-tandem mass ScanMode (FullScan and SelectedIonMonitoring) and other massspectrometer (ESI-QTOF and MALDI-TOF), this option is resolved to Null.

Default Value: Automatic

Default Calculation: For TripleQuandrupole as the MassAnalyzer, is set to first CollisionCellExitVoltage, otherwise set to Null.

Pattern Description: Greater than or equal to -55 volts and less than or equal to 55 volts or Null.

Programmatic Pattern: (RangeP\[-55\*Volt, 55\*Volt\] | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeMassDetectionStepSize**

Indicate the step size for mass collection in range when using TripleQuadruploe as the MassAnalyzer.

Default Value: Automatic

Default Calculation: Is set to first CollisionCellExitVoltage

Pattern Description: Greater than or equal to 0.01 grams per mole and less than or equal to 1 gram per mole or Null.

Programmatic Pattern: (RangeP\[(0.01\*Gram)/Mole, (1\*Gram)/Mole\] | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeMultipleReactionMonitoringAssays**

In ESI-QQQ mass spectrometry analysis, the ion corresponding to the compound of interest is targetted with subsequent fragmentation of that target ion to produce a range of daughter ions. One (or more) of these fragment daughter ions can be selected for quantitation purposes. Only compounds that meet both these criteria, i.e. specific parent ion and specific daughter ions corresponding to the mass of the molecule of interest are detected within the mass spectrometer. The mass assays (MS1/MS2 mass value combinations) for each scan, along with the CollisionEnergy and DwellTime (length of time of each scan).

Default Value: Automatic

Default Calculation: Is set based one ColumnPrimeMassDetection, ColumnPrimeCollissionEnergy, ColumnPrimeDwellTime and ColumnPrimeFramentMassDetection.

Pattern Description: List of one or more Individual Multiple Reaction Monitoring Assay or None entries or Null or Null.

Programmatic Pattern: (({({GreaterP\[(0\*Gram)/Mole\], (RangeP\[5\*Volt, 180\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\]) | Automatic, GreaterP\[(0\*Gram)/Mole\], GreaterP\[0\*Second\] | Automatic} | Null)..} | Null) | Automatic) | Null

Index Matches to: ColumnPrimeAcquisitionWindow

#### **ColumnPrimeAbsorbanceWavelength**

The physical properties of light passed through the flow for measurement with the PhotoDiodeArray (PDA) Detector.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in AbsorbanceWavelength.

Pattern Description: All or Range or Single or Null.

Programmatic Pattern: ((RangeP\[190\*Nanometer, 500\*Nanometer, 1\*Nanometer\] | All | RangeP\[190\*Nanometer, 490\*Nanometer, 1\*Nanometer\] ;; RangeP\[200\*Nanometer, 500\*Nanometer, 1\*Nanometer\]) | Automatic) | Null

#### **ColumnPrimeWavelengthResolution**

The increment of wavelength for the range of light passed through the flow for absorbance measurement with the photo diode array (PDA) detector for ColumnPrime measurements.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in WavelengthResolution.

Pattern Description: Greater than or equal to 1.2 nanometers and less than or equal to 12. nanometers or Null.

Programmatic Pattern: (RangeP\[1.2\*Nanometer, 12.\*Nanometer\] | Automatic) | Null

#### **ColumnPrimeUVFilter**

Indicates if UV wavelengths (less than 210 nm) should be blocked from being transmitted through the sample for the PhotoDiodeArray (PDA) detector for ColumnPrime measurements.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in UVFilter.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

#### **ColumnPrimeAbsorbanceSamplingRate**

The frequency of ColumnPrime measurement. Lower values will be less susceptible to noise but will record less frequently across time.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in AbsorbanceSamplingRate.

Pattern Description: Greater than or equal to 1 reciprocal second and less than or equal to 80 reciprocal seconds in increments of 1 reciprocal second or Null.

Programmatic Pattern: (RangeP\[(1\*1)/Second, (80\*1)/Second, (1\*1)/Second\] | Automatic) | Null

### ColumnFlush

#### **ColumnFlushTemperature**

The column's temperature at which the column flush gradient is run.

Default Value: Automatic

Default Calculation: Automatically set from ColumnTemperature. Automatic resolution can be inherited from the ColumnFlushGradient option.

Pattern Description: Ambient or greater than or equal to 5 degrees Celsius and less than or equal to 80 degrees Celsius or Null.

Programmatic Pattern: ((RangeP\[5\*Celsius, 80\*Celsius\] | Ambient) | Automatic) | Null

#### **ColumnFlushGradientA**

The composition of BufferA within the flow, defined for specific time points for column flush.

Default Value: Automatic

Default Calculation: Automatically set from ColumnFlushGradient option or implicitly resolved from ColumnFlushGradientB, ColumnFlushGradientC, and ColumnFlushGradientD options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer A Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

#### **ColumnFlushGradientB**

The composition of BufferB within the flow, defined for specific time points for column flush.

Default Value: Automatic

Default Calculation: Automatically set from ColumnFlushGradient option or implicitly resolved from ColumnFlushGradientA, ColumnFlushGradientC, and ColumnFlushGradientD options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer B Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

#### **ColumnFlushGradientC**

The composition of BufferC within the flow, defined for specific time points for column flush.

Default Value: Automatic

Default Calculation: Automatically set from ColumnFlushGradient option or implicitly resolved from ColumnFlushGradientA, ColumnFlushGradientB, and ColumnFlushGradientD options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer C Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

#### **ColumnFlushGradientD**

The composition of BufferD within the flow, defined for specific time points for column flush.

Default Value: Automatic

Default Calculation: Automatically set from ColumnFlushGradient option or implicitly resolved from ColumnFlushGradientA, ColumnFlushGradientB, and ColumnFlushGradientC options.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer D Composition} entries or Null.

Programmatic Pattern: ((RangeP\[0\*Percent, 100\*Percent\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\]}..}) | Automatic) | Null

#### **ColumnFlushFlowRate**

The speed of the fluid through the system for column flush.

Default Value: Automatic

Default Calculation: Automatically set from Type and Scale or inherited from the method given in the ColumnFlushGradient option.

Pattern Description: Greater than or equal to 0 milliliters per minute and less than or equal to 2 milliliters per minute or list of one or more {Time, Flow Rate} entries or Null.

Programmatic Pattern: ((RangeP\[(0\*Milliliter)/Minute, (2\*Milliliter)/Minute\] | {{GreaterEqualP\[0\*Minute\], RangeP\[(0\*Milliliter)/Minute, (2\*Milliliter)/Minute\]}..}) | Automatic) | Null

#### **ColumnFlushStart**

A shorthand option to specify the starting BufferB composition for column flush runs. This option must be specified with ColumnFlushEnd and ColumnFlushDuration.

Default Value: Null

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or Null.

Programmatic Pattern: RangeP\[0\*Percent, 100\*Percent\] | Null

#### **ColumnFlushEnd**

A shorthand option to specify the final BufferB composition for column flush runs. This option must be specified with ColumnFlushStart and ColumnFlushDuration.

Default Value: Null

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or Null.

Programmatic Pattern: RangeP\[0\*Percent, 100\*Percent\] | Null

#### **ColumnFlushDuration**

A shorthand option to specify the duration of the column flush gradient.

Default Value: Null

Pattern Description: Greater than or equal to 0 minutes or Null.

Programmatic Pattern: GreaterEqualP\[0\*Minute\] | Null

#### **ColumnFlushGradient**

The buffer composition over time in the fluid flow for column flush.

Default Value: Automatic

Default Calculation: Automatically set to best meet all the ColumnFlushGradient\_ options (e.g. ColumnFlushGradientA, ColumnFlushGradientB, ColumnFlushGradientC, ColumnFlushGradientD, ColumnFlushDuration).

Pattern Description: An object of type or subtype Object\[Method, Gradient\] or list of one or more {Time, Buffer A Composition, Buffer B Composition, Buffer C Composition, Buffer D Composition, Flow Rate} entries or Null.

Programmatic Pattern: ((ObjectP\[Object\[Method, Gradient\]\] | {{GreaterEqualP\[0\*Minute\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[0\*Percent, 100\*Percent\], RangeP\[(0\*Milliliter)/Minute, (2\*Milliliter)/Minute\]}..}) | Automatic) | Null

#### **ColumnFlushIonMode**

Indicates if positively or negatively charged ions are analyzed.

Default Value: Automatic

Default Calculation: Set to the first IonMode for an analyte input sample.

Pattern Description: Negative or Positive or Null.

Programmatic Pattern: (IonModeP | Automatic) | Null

#### **ColumnFlushMassSpectrometryMethod**

The previously specified instruction(s) for the analyte ionization, selection, fragmentation, and detection.

Default Value: Automatic

Default Calculation: If ColumnFlush samples exist and MassSpectrometryMethod is specified, then set to the first available ColumnFlushMassSpectrometryMethod.

Pattern Description: An object of type or subtype Object\[Method, MassAcquisition\] or New or Null.

Programmatic Pattern: ((ObjectP\[Object\[Method, MassAcquisition\]\] | New) | Automatic) | Null

#### **ColumnFlushESICapillaryVoltage**

The absolute voltage applied to the tip of the stainless steel capillary tubing in order to produce charged droplets. Adjust this voltage to maximize sensitivity. Most compounds are optimized between 0.5 and 3.2 kV in ESI positive ion mode and 0.5 and 2.6 in ESI negative ion mode, but can be altered according to sample type. For low flow applications, best sensitivity will be achieved with a relatively high value in ESI positive (e.g. 3.0 kV), for columnFlush flow UPLC a value of 0.5 kV is typically best for maximum sensitivity.

Default Value: Automatic

Default Calculation: Is automatically set to the first ESICapillaryVoltage.

Pattern Description: Greater than or equal to -4 kilovolts and less than or equal to 5 kilovolts or Null.

Programmatic Pattern: (RangeP\[-4\*Kilovolt, 5\*Kilovolt\] | Automatic) | Null

#### **ColumnFlushDeclusteringVoltage**

The voltage offset between the ion block (the reduced pressure chamber of the source block) and the stepwave ion guide (the optics before the quadrupole mass analyzer). This voltage attracts charged ions in the spray being produced from the capillary tip into the ion block leading into the mass spectrometer. This voltage is typically set to 25-100 V and its tuning has little effect on sensitivity compared to other options (e.g. ColumnFlushStepwaveVoltage).

Default Value: Automatic

Default Calculation: Is automatically set to any specified MassAcquisition method; otherwise, set to 40 Volt.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 150 volts or Null.

Programmatic Pattern: (RangeP\[0.1\*Volt, 150\*Volt\] | Automatic) | Null

#### **ColumnFlushStepwaveVoltage**

The voltage offset between the 1st and 2nd stage of the stepwave ion guide which leads ions coming from the sample cone towards the quadrupole mass analyzer. This voltage normally optimizes between 25 and 150 V and should be adjusted for sensitivity depending on compound and charge state. For multiply charged species it is typically set to to 40-50 V, and higher for singly charged species. In general higher cone voltages (120-150 V) are needed for larger mass ions such as intact proteins and monoclonal antibodies. It also has greatest effect on in-source fragmentation and should be decreased if in-source fragmentation is observed but not desired.

Default Value: Automatic

Default Calculation: Is automatically set to the first StepwaveVoltage.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 200 volts or Null.

Programmatic Pattern: (RangeP\[0.1\*Volt, 200\*Volt\] | Automatic) | Null

#### **ColumnFlushSourceTemperature**

The temperature setting of the source block. Heating the source block discourages condensation and decreases solvent clustering in the reduced vacuum region of the source. This temperature setting is flow rate and sample dependent. Typical values are between 60 to 120 Celsius. For thermally labile analytes, a lower temperature setting is recommended.

Default Value: Automatic

Default Calculation: Is automatically set to the first SourceTemperature.

Pattern Description: Greater than or equal to 25 degrees Celsius and less than or equal to 150 degrees Celsius or Null.

Programmatic Pattern: (RangeP\[25\*Celsius, 150\*Celsius\] | Automatic) | Null

#### **ColumnFlushDesolvationTemperature**

The temperature setting for the ESI desolvation heater that controls the nitrogen gas temperature used for solvent evaporation to produce single gas phase ions from the ion spray. Similar to ColumnFlushDesolvationGasFlow, this setting is dependent on solvent flow rate and composition. A typical range is from 150 to 650 Celsius.

Default Value: Automatic

Default Calculation: Is automatically set to the first DesolvationTemperature.

Pattern Description: Greater than or equal to 20 degrees Celsius and less than or equal to 650 degrees Celsius or Null.

Programmatic Pattern: (RangeP\[20\*Celsius, 650\*Celsius\] | Automatic) | Null

#### **ColumnFlushDesolvationGasFlow**

The rate at which nitrogen gas is flowed around the ESI capillary. It is used for solvent evaporation to produce single gas phase ions from the ion spray. Similar to ColumnFlushDesolvationTemperature, this setting is dependent on solvent flow rate and composition. Higher desolvation temperatures usually result in increased sensitivity, but too high values can cause spray instability. Typical values are between 300 to 1200 L/h.

Default Value: Automatic

Default Calculation: Is automatically set to the first DesolvationGasFlow.

Pattern Description: Greater than or equal to 55 liters per hour and less than or equal to 1200 liters per hour or greater than or equal to 0 pounds‐force per inch squared and less than or equal to 85 pounds‐force per inch squared or Null.

Programmatic Pattern: ((RangeP\[(55\*Liter)/Hour, (1200\*Liter)/Hour\] | RangeP\[0\*PSI, 85\*PSI\]) | Automatic) | Null

#### **ColumnFlushConeGasFlow**

The rate at which nitrogen gas is flowed around the sample inlet cone (the spherical metal plate acting as a first gate between the sprayer and the reduced pressure chamber, the ion block). This gas flow is used to minimize the formation of solvent ion clusters. It also helps reduce adduct ions and directing the spray into the ion block while keeping the sample cone clean. Typical values are between 0 and 150 L/h.

Default Value: Automatic

Default Calculation: Is automatically set to the first ConeGasFlow.

Pattern Description: Greater than or equal to 0 liters per hour and less than or equal to 300 liters per hour or greater than or equal to 30 pounds‐force per inch squared and less than or equal to 50 pounds‐force per inch squared or Null.

Programmatic Pattern: ((RangeP\[(0\*Liter)/Hour, (300\*Liter)/Hour\] | RangeP\[30\*PSI, 50\*PSI\]) | Automatic) | Null

#### **ColumnFlushAcquisitionWindow**

The time range with respect to the the chromatographic separation to conduct analyte ionization, selection/survey, optional fragmentation, and detection.

Default Value: Automatic

Default Calculation: Set to the entire gradient window 0 Minute to the last time point in ColumnFlushGradient.

Pattern Description: A span from anything greater than or equal to 0 minutes and less than or equal to 8 hours to anything greater than or equal to 0 minutes and less than or equal to 8 hours or Null.

Programmatic Pattern: (RangeP\[0\*Minute, 8\*Hour\] ;; RangeP\[0\*Minute, 8\*Hour\] | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushAcquisitionMode**

The method by which spectra are collected. DataDependent will depend on the properties of the measured mass spectrum of the intact ions. DataIndependent will systemically scan through all of the intact ions. MS1FullScan will focus on defined intact masses. MS1MS2 will focus on fragmented masses.

Default Value: Automatic

Default Calculation: Set to MS1FullScan unless DataDependent related options are set, then set to DataDependent.

Pattern Description: DataIndependent, DataDependent, MS1FullScan, MS1MS2ProductIonScan, SelectedIonMonitoring, NeutralIonLoss, PrecursorIonScan, or MultipleReactionMonitoring or Null.

Programmatic Pattern: (MSAcquisitionModeP | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushFragment**

Indicates if ions should be collided with neutral gas and dissociated in order to measure the resulting product ions. Also known as tandem mass spectrometry or MS/MS (as opposed to MS).

Default Value: Automatic

Default Calculation: Set to True if ColumnFlushAcquisitionMode is MS1MS2ProductIonScan, DataDependent, or DataIndependent. Set True if any of the Fragmentation related options are set (e.g. ColumnFlushFragmentMassDetection).

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushMassDetection**

The lowest and the highest mass-to-charge ratio (m/z) to be recorded or selected for intact masses. When ColumnFlushFragment is True, the intact ions will be selected for fragmentation.

Default Value: Automatic

Default Calculation: For ColumnFlushFragment -> False, automatically set to one of three default mass ranges according to the molecular weight of the ColumnFlushAnalytes to encompass them.

Pattern Description: All or Range or Single or Specific List or Null.

Programmatic Pattern: ((RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | {RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]..} | RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] ;; RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\] | MSAnalyteGroupP) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushScanTime**

The duration of time allowed to pass between each spectral acquisition. When ColumnFlushAcquisitionMode is DataDependent, this value refers to the duration for measuring spectra from the intact ions. Increasing this value improves sensitivity whereas decreasing this value allows for more data points and spectra to be acquired.

Default Value: Automatic

Default Calculation: Set to 0.2 seconds unless a method is given.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 10 seconds.

Programmatic Pattern: RangeP\[0.015\*Second, 10\*Second\] | Automatic

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushFragmentMassDetection**

The lowest and the highest mass-to-charge ratio (m/z) to be recorded or selected for product ions. When ColumnFlushAcquisitionMode is DataDependent|DataIndependent, all of the product ions in consideration for measurement. Null if ColumnFlushFragment is False.

Default Value: Automatic

Default Calculation: When ColumnFlushFragment is False, set to Null. Otherwise, 20 Gram/Mole to the maximum ColumnFlushMassDetection.

Pattern Description: All or Range or Specific or Null.

Programmatic Pattern: (({RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\]..} | All | RangeP\[(20\*Gram)/Mole, (16000\*Gram)/Mole\] ;; RangeP\[(100\*Gram)/Mole, (16000\*Gram)/Mole\]) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushCollisionEnergy**

The voltage by which intact ions are accelerated through inert gas in order to dissociate them into measurable fragment ion species when ColumnFlushFragment is True. Cannot be defined simultaneously with ColumnFlushCollisionEnergyMassProfile.

Default Value: Automatic

Default Calculation: Is automatically set to 40 Volt when ColumnFlushFragment is True, otherwise is set to Null.

Pattern Description: Greater than or equal to 5 volts and less than or equal to 255 volts or greater than or equal to -180 volts and less than or equal to 5 volts or list of one or more greater than or equal to 5 volts and less than or equal to 180 volts or greater than or equal to -180 volts and less than or equal to 5 volts entries or Null.

Programmatic Pattern: (((RangeP\[5\*Volt, 255\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\]) | {(RangeP\[5\*Volt, 180\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\])..}) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushCollisionEnergyMassProfile**

The relationship of collision energy with the ColumnFlushMassDetection.

Default Value: Automatic

Default Calculation: Set to ColumnFlushCollisionEnergyMassScan if defined; otherwise, set to Null.

Pattern Description: A span from anything greater than or equal to 0.1 volts and less than or equal to 255 volts to anything greater than or equal to 0.1 volts and less than or equal to 255 volts or Null.

Programmatic Pattern: (RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\] | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushCollisionEnergyMassScan**

The collision energy profile at the end of the scan from ColumnFlushCollisionEnergy or ColumnFlushCollisionEnergyScanProfile, as related to analyte mass.

Default Value: Automatic

Pattern Description: Constant or Range or Null.

Programmatic Pattern: ((RangeP\[0.1\*Volt, 255\*Volt\] | RangeP\[0.1\*Volt, 255\*Volt\] ;; RangeP\[0.1\*Volt, 255\*Volt\]) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushFragmentScanTime**

The duration of the spectral scanning for each fragmentation of an intact ion when ColumnFlushAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Automatically set to the same value as ScanTime if ColumnFlushAcquisitionMode is DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 10 seconds or Null.

Programmatic Pattern: ((Alternatives\[RangeP\[0.015\*Second, 10\*Second\]\]) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushAcquisitionSurvey**

The number of intact ions to consider for fragmentation and product ion measurement in every measurement cycle when ColumnFlushAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Automatically set to 10 if ColumnFlushAcquisitionMode is set to DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 1 and less than or equal to 30 in increments of 1 or Null.

Programmatic Pattern: (RangeP\[1, 30, 1\] | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushMinimumThreshold**

The minimum number of total ions detected within ScanTime durations needed to trigger the start of data dependent acquisition when ColumnFlushAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Automatically set to (100000/Second)\*ScanTime if ColumnFlushAcquisitionMode is DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or Null.

Programmatic Pattern: (RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushAcquisitionLimit**

The maximum number of total ions for a specific intact ion when ColumnFlushAcquisitionMode is set to DataDependent. When this value is exceeded, acquisition will switch to fragmentation of the next candidate ion.

Default Value: Automatic

Default Calculation: Automatically inherited from supplied method if ColumnFlushAcquisitionMode is set to DataDependent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 ArbitraryUnits and less than or equal to 8000000 ArbitraryUnits or Null.

Programmatic Pattern: (RangeP\[0\*ArbitraryUnit, 8000000\*ArbitraryUnit\] | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushCycleTimeLimit**

The maximum possible computed duration of all of the scans for the intact and fragmentation measurements when ColumnFlushAcquisitionMode is set to DataDependent.

Default Value: Automatic

Default Calculation: Calculated from the ColumnFlushAcquisitionSurvey, ColumnFlushScanTime, and ColumnFlushFragmentScanTime.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 20000 seconds or Null.

Programmatic Pattern: (RangeP\[0.015\*Second, 20000\*Second\] | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushExclusionDomain**

The tune range when the ColumnFlushExclusionMasses are omitted in the chromatogram. Full indicates for the entire period.

Default Value: Automatic

Default Calculation: Set to the entire ColumnFlushAcquisitionWindow.

Pattern Description: A span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full entries or Null.

Programmatic Pattern: (((GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full) | {(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full)..}) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushExclusionMass**

The intact ions (Target Mass) to omit. When the Mode is set to All, the mass is excluded for the entire ExclusionDomain. When the Mode is set to Once, the Mass is excluded in the first survey appearance, but considered for consequent ones.

Default Value: Automatic

Default Calculation: If any ColumnFlushExclusionMode-related options are set (e.g. ColumnFlushExclusionMassTolerance), a target mass of the first Analyte (if not in ColumnFlushInclusionMasses) is chosen and retention time is set to 0\*Minute.

Pattern Description: List of one or more {Mode, Target Mass} entries or {Mode, Target Mass} or Null.

Programmatic Pattern: (({All | Once, RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]} | {{All | Once, RangeP\[(2\*Gram)/Mole, (100000\*Gram)/Mole\]}..}) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushExclusionMassTolerance**

The range above and below each ion in ColumnFlushExclusionMasses to consider for omission when ColumnFlushExclusionMass is set to All or Once.

Default Value: Automatic

Default Calculation: If ColumnFlushExclusionMass -> All or Once, set to 0.5 Gram/Mole; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null.

Programmatic Pattern: (RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushExclusionRetentionTimeTolerance**

The range of time above and below the ColumnFlushExclusionDomain to consider for exclusion.

Default Value: Automatic

Default Calculation: If ColumnFlushExclusionMass and ColumnFlushExclusionDomain options are set, this is set to 10 seconds; otherwise, Null.

Pattern Description: Greater than or equal to 0 seconds and less than or equal to 3600 seconds or Null.

Programmatic Pattern: (RangeP\[0\*Second, 3600\*Second\] | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushInclusionDomain**

The time range when the ColumnFlushInclusionMass applies with respect to the chromatogram.

Default Value: Automatic

Default Calculation: Set to the entire ColumnFlushAcquisitionWindow.

Pattern Description: A span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full or list of one or more a span from anything greater than or equal to 0 minutes to anything greater than or equal to 0 minutes or Full entries or Null.

Programmatic Pattern: (((GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full) | {(GreaterEqualP\[0\*Minute\] ;; GreaterEqualP\[0\*Minute\] | Full)..}) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushInclusionMass**

The ions (Target Mass) to prioritize during the survey scan for further fragmentation When ColumnFlushAcquisitionMode is DataDependent. ColumnFlushInclusionMass set to Only will solely be considered for surveys. When Mode is Preferential, the InclusionMass will be prioritized for survey.

Default Value: Automatic

Default Calculation: When ColumnFlushInclusionMode Only or Preferential, an entry mass is added based on the mass of the most salient analyte of the sample.

Pattern Description: List of one or more {Mode, Target Mass} entries or {Mode, Target Mass} or Null.

Programmatic Pattern: (({Only | Preferential, RangeP\[(2\*Gram)/Mole, (4000\*Gram)/Mole\]} | {{Only | Preferential, RangeP\[(2\*Gram)/Mole, (4000\*Gram)/Mole\]}..}) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushInclusionCollisionEnergy**

The overriding collision energy value that can be applied to the the ColumnFlushInclusionMass. Null will default to the ColumnFlushCollisionEnergy option and related.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0 volts and less than or equal to 255 volts or list of one or more greater than or equal to 0 volts and less than or equal to 255 volts entries or Null.

Programmatic Pattern: ((RangeP\[0\*Volt, 255\*Volt\] | {RangeP\[0\*Volt, 255\*Volt\]..}) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushInclusionDeclusteringVoltage**

The overriding source voltage value that can be applied to the the ColumnFlushInclusionMass. Null will default to the ColumnFlushDeclusteringVoltage option.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0.1 volts and less than or equal to 150 volts or list of one or more greater than or equal to 0.1 volts and less than or equal to 150 volts entries or Null.

Programmatic Pattern: ((RangeP\[0.1\*Volt, 150\*Volt\] | {RangeP\[0.1\*Volt, 150\*Volt\]..}) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushInclusionChargeState**

The maximum charge state of the ColumnFlushInclusionMass to also consider for inclusion. For example, if this is set to 3 and the polarity is Positive, then +1,+2,+3 charge states will be considered as well.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0 and less than or equal to 6 in increments of 1 or list of one or more greater than or equal to 0 and less than or equal to 6 in increments of 1 entries or Null.

Programmatic Pattern: ((RangeP\[0, 6, 1\] | {RangeP\[0, 6, 1\]..}) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushInclusionScanTime**

The overriding scan time duration that can be applied to the the ColumnFlushInclusionMass for the consequent fragmentation. Null will default to the ColumnFlushFragmentScanTime option.

Default Value: Automatic

Default Calculation: Inherited from any supplied method.

Pattern Description: Greater than or equal to 0.015 seconds and less than or equal to 10 seconds or list of one or more greater than or equal to 0.015 seconds and less than or equal to 10 seconds entries or Null.

Programmatic Pattern: ((RangeP\[0.015\*Second, 10\*Second\] | {RangeP\[0.015\*Second, 10\*Second\]..}) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushInclusionMassTolerance**

The range above and below each ion in ColumnFlushInclusionMass to consider for prioritization. For example, if set to 0.5 Gram/Mole, the total range is 1 Gram/Mole.

Default Value: Automatic

Default Calculation: Set to 0.5 Gram/Mole if ColumnFlushInclusionMass is given; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null.

Programmatic Pattern: ((Alternatives\[RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\]\]) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushSurveyChargeStateExclusion**

Indicates if redundant ions that differ by ionic charge (+1/-1, +2/-2, etc.) should be excluded and if ColumnFlushChargeState exclusion-related options should be automatically filled in.

Default Value: Automatic

Default Calculation: Set to True, if any of the ColumnFlushChargeState options are set; otherwise, False.

Pattern Description: True or False or Null.

Programmatic Pattern: ((Alternatives\[BooleanP\]) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushSurveyIsotopeExclusion**

Indicates if redundant ions that differ by isotopic mass (e.g. 1, 2 Gram/Mole) should be excluded and if ColumnFlushMassIsotope exclusion-related options should be automatically filled.

Default Value: Automatic

Default Calculation: Set to True, if any of the ColumnFlushIsotopeExclusion options are set; otherwise, False.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushChargeStateExclusionLimit**

The number of ions to survey first with exclusion by ionic state. For example, if ColumnFlushAcquisitionSurvey is 10 and this option is 5, then 5 ions will be surveyed with charge-state exclusion. For candidate ions of rank 6 to 10, no exclusion will be performed.

Default Value: Automatic

Default Calculation: Inherited from any supplied method; otherwise, set the same to ColumnFlushAcquisitionSurvey, if any ChargeState option is set.

Pattern Description: Greater than or equal to 0 and less than or equal to 30 in increments of 1 or Null.

Programmatic Pattern: (RangeP\[0, 30, 1\] | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushChargeStateExclusion**

The specific ionic states of intact ions to redundantly exclude from the survey for further fragmentation/acquisition. 1 refers to +1/-1, 2 refers to +2/-2, etc.

Default Value: Automatic

Default Calculation: When ColumnFlushSurveyChargeStateExclusion is True, set to {1,2}; otherwise, Null.

Pattern Description: Greater than or equal to 1 and less than or equal to 6 in increments of 1 or list of one or more greater than or equal to 1 and less than or equal to 6 in increments of 1 entries or Null.

Programmatic Pattern: ((RangeP\[1, 6, 1\] | {RangeP\[1, 6, 1\]..}) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushChargeStateMassTolerance**

The range of m/z to consider for exclusion by ionic state property when ColumnFlushSurveyChargeStateExclusion is True.

Default Value: Automatic

Default Calculation: When ColumnFlushSurveyChargeStateExclusion is True, set to 0.5 Gram/Mole; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null.

Programmatic Pattern: (RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\] | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushIsotopicExclusion**

The m/z difference between monoisotopic ions as a criterion for survey exclusion.

Default Value: Automatic

Default Calculation: When ColumnFlushSurveyIsotopeExclusion is True, set to 1 Gram/Mole; otherwise, Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or list of one or more greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole entries or Null.

Programmatic Pattern: (((Alternatives\[RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\]\]) | {(Alternatives\[RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\]\])..}) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushIsotopeRatioThreshold**

The minimum relative magnitude between monoisotopic ions in order to be considered an isotope for exclusion.

Default Value: Automatic

Default Calculation: When ColumnFlushSurveyIsotopeExclusion is True, set to 0.1; otherwise, Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or list of one or more greater than or equal to 0 and less than or equal to 1 entries or Null.

Programmatic Pattern: ((RangeP\[0, 1\] | {RangeP\[0, 1\]..}) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushIsotopeDetectionMinimum**

The acquisition rate of a given intact mass to consider for isotope exclusion in the survey.

Default Value: Automatic

Default Calculation: When ColumnFlushSurveyIsotopeExclusion is True, set to 10 1/Second; otherwise, Null.

Pattern Description: Greater than or equal to 0 reciprocal seconds or list of one or more greater than or equal to 0 reciprocal seconds entries or Null.

Programmatic Pattern: ((GreaterEqualP\[(0\*1)/Second\] | {GreaterEqualP\[(0\*1)/Second\]..}) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushIsotopeMassTolerance**

The range of m/z around a mass to consider for exclusion. This applies for both ChargeState and mass shifted Isotope. If set to 0.5 Gram/Mole, then the total range should be 1 Gram/Mole.

Default Value: Automatic

Default Calculation: When ColumnFlushSurveyIsotopeExclusion or ColumnFlushSurveyChargeStateExclusion is True, set to 0.5 Gram/Mole; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 grams per mole and less than or equal to 3000 grams per mole or Null.

Programmatic Pattern: ((Alternatives\[RangeP\[(0\*Gram)/Mole, (3000\*Gram)/Mole\]\]) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushIsotopeRatioTolerance**

The range of relative magnitude around ColumnFlushIsotopeRatio to consider for isotope exclusion.

Default Value: Automatic

Default Calculation: If ColumnFlushSurveyIsotopeExclusion is True, set to 30\*Percent; otherwise, set to Null.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or Null.

Programmatic Pattern: ((Alternatives\[RangeP\[0\*Percent, 100\*Percent\]\]) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushNeutralLoss**

A neutral loss scan is performed on ESI-QQQ mass spectrometry by scanning the sample through the first quadrupole (Q1). The ions are then fragmented in the collision cell. The second mass analyzer is then scanned with a fixed offset to MS1. This option represents the value of this offset.

Default Value: Automatic

Default Calculation: Is set to 500 g/mol if using NeutralIonLoss as the ColumnFlushAcquisitionMode, and is Null in other modes.

Pattern Description: Greater than 0 grams per mole or Null.

Programmatic Pattern: (GreaterP\[(0\*Gram)/Mole\] | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushDwellTime**

The duration of time for which spectra are acquired at the specific mass detection value for SelectedIonMonitoring and MultipleReactionMonitoring mode in ESI-QQQ.

Default Value: Automatic

Default Calculation: Is automatically set to 200 microsecond if ColumnFlushAcquisitionMode is in SelectedIonMonitoring or MultipleReactionMonitoring mode.

Pattern Description: Greater than or equal to 5 milliseconds and less than or equal to 2000 milliseconds or list of one or more greater than or equal to 5 milliseconds and less than or equal to 2000 milliseconds entries or Null.

Programmatic Pattern: ((RangeP\[5\*Millisecond, 2000\*Millisecond\] | {RangeP\[5\*Millisecond, 2000\*Millisecond\]..}) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushCollisionCellExitVoltage**

Also known as the Collision Cell Exit Potential (CXP). This value focuses and accelerates the ions out of collision cell (Q2) and into 2nd mass analyzer (MS 2). This potential is tuned to ensure successful ion acceleration out of collision cell and into MS2, and can be adjusted to reach the maximal signal intensity. This option is unique to ESI-QQQ for now, and only required when Fragment ->True and/or in ScanMode that achieves tandem mass feature (PrecursorIonScan, NeutralIonLoss,ProductIonScan,MultipleReactionMonitoring). For non-tandem mass ScanMode (FullScan and SelectedIonMonitoring) and other massspectrometer (ESI-QTOF and MALDI-TOF), this option is resolved to Null.

Default Value: Automatic

Default Calculation: For TripleQuandrupole as the MassAnalyzer, is set to first CollisionCellExitVoltage, otherwise set to Null.

Pattern Description: Greater than or equal to -55 volts and less than or equal to 55 volts or Null.

Programmatic Pattern: (RangeP\[-55\*Volt, 55\*Volt\] | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushMassDetectionStepSize**

Indicate the step size for mass collection in range when using TripleQuadruploe as the MassAnalyzer.

Default Value: Automatic

Default Calculation: Is set to first CollisionCellExitVoltage

Pattern Description: Greater than or equal to 0.01 grams per mole and less than or equal to 1 gram per mole or Null.

Programmatic Pattern: (RangeP\[(0.01\*Gram)/Mole, (1\*Gram)/Mole\] | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushMultipleReactionMonitoringAssays**

In ESI-QQQ mass spectrometry analysis, the ion corresponding to the compound of interest is targetted with subsequent fragmentation of that target ion to produce a range of daughter ions. One (or more) of these fragment daughter ions can be selected for quantitation purposes. Only compounds that meet both these criteria, i.e. specific parent ion and specific daughter ions corresponding to the mass of the molecule of interest are detected within the mass spectrometer. The mass assays (MS1/MS2 mass value combinations) for each scan, along with the CollisionEnergy and DwellTime (length of time of each scan).

Default Value: Automatic

Default Calculation: Is set based one ColumnFlushMassDetection, ColumnFlushCollissionEnergy, ColumnFlushDwellTime and ColumnFlushFramentMassDetection.

Pattern Description: List of one or more Individual Multiple Reaction Monitoring Assay or None entries or Null or Null.

Programmatic Pattern: (({({GreaterP\[(0\*Gram)/Mole\], (RangeP\[5\*Volt, 180\*Volt\] | RangeP\[-180\*Volt, 5\*Volt\]) | Automatic, GreaterP\[(0\*Gram)/Mole\], GreaterP\[0\*Second\] | Automatic} | Null)..} | Null) | Automatic) | Null

Index Matches to: ColumnFlushAcquisitionWindow

#### **ColumnFlushAbsorbanceWavelength**

The physical properties of light passed through the flow for measurement with the PhotoDiodeArray (PDA) Detector for ColumnFlush measurement.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in AbsorbanceWavelength.

Pattern Description: All or Range or Single or Null.

Programmatic Pattern: ((RangeP\[190\*Nanometer, 500\*Nanometer, 1\*Nanometer\] | All | RangeP\[190\*Nanometer, 490\*Nanometer, 1\*Nanometer\] ;; RangeP\[200\*Nanometer, 500\*Nanometer, 1\*Nanometer\]) | Automatic) | Null

#### **ColumnFlushWavelengthResolution**

The increment of wavelength for the range of light passed through the flow for absorbance measurement with the photo diode array (PDA) detector for ColumnFlush measurement.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in WavelengthResolution.

Pattern Description: Greater than or equal to 1.2 nanometers and less than or equal to 12. nanometers or Null.

Programmatic Pattern: (RangeP\[1.2\*Nanometer, 12.\*Nanometer\] | Automatic) | Null

#### **ColumnFlushUVFilter**

Indicates if UV wavelengths (less than 210 nm) should be blocked from being transmitted through the sample for the PhotoDiodeArray (PDA) detector for ColumnFlush measurement.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in UVFilter.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

#### **ColumnFlushAbsorbanceSamplingRate**

The frequency of ColumnFlush measurement. Lower values will be less susceptible to noise but will record less frequently across time.

Default Value: Automatic

Default Calculation: Automatically set to the same as the first entry in AbsorbanceSamplingRate.

Pattern Description: Greater than or equal to 1 reciprocal second and less than or equal to 80 reciprocal seconds in increments of 1 reciprocal second or Null.

Programmatic Pattern: (RangeP\[(1\*1)/Second, (80\*1)/Second, (1\*1)/Second\] | Automatic) | Null

Sample Prep Options
===================

### Sample Preparation

#### **PreparatoryUnitOperations**

Specifies a sequence of transferring, aliquoting, consolidating, or mixing of new or existing samples before the main experiment. These prepared samples can be used in the main experiment by referencing their defined name. For more information, please reference the documentation for ExperimentSampleManipulation.

Default Value: Null

Pattern Description: List of one or more unit Operation ManualSamplePreparation or RoboticSamplePreparation or unit Operation must match SamplePreparationP entries or Null.

Programmatic Pattern: {((ManualSamplePreparationMethodP | RoboticSamplePreparationMethodP) | SamplePreparationP)..} | Null

#### **PreparatoryPrimitives**

Specifies a sequence of transferring, aliquoting, consolidating, or mixing of new or existing samples before the main experiment. These prepared samples can be used in the main experiment by referencing their defined name. For more information, please reference the documentation for ExperimentSampleManipulation.

Default Value: Null

Pattern Description: List of one or more a primitive with head Define, Transfer, Mix, Aliquot, Consolidation, FillToVolume, Incubate, Filter, Wait, Centrifuge, or Resuspend entries or Null.

Programmatic Pattern: {SampleManipulationP..} | Null

### Preparatory Incubation

#### **Incubate**

Indicates if the SamplesIn should be incubated at a fixed temperature prior to starting the experiment or any aliquoting. Sample Preparation occurs in the order of Incubation, Centrifugation, Filtration, and then Aliquoting (if specified).

Default Value: Automatic

Default Calculation: Resolves to True if any of the corresponding Incubation options are set. Otherwise, resolves to False.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

#### **IncubationTemperature**

Temperature at which the SamplesIn should be incubated for the duration of the IncubationTime prior to starting the experiment.

Default Value: Automatic

Pattern Description: Ambient or greater than or equal to -20 degrees Celsius and less than or equal to 500 degrees Celsius or Null.

Programmatic Pattern: ((Ambient | RangeP\[$MinIncubationTemperature, $MaxIncubationTemperature\]) | Automatic) | Null

Index Matches to: experiment samples

#### **IncubationTime**

Duration for which SamplesIn should be incubated at the IncubationTemperature, prior to starting the experiment.

Default Value: Automatic

Pattern Description: Greater than or equal to 1 minute and less than or equal to 72 hours or Null.

Programmatic Pattern: (RangeP\[1\*Minute, $MaxExperimentTime\] | Automatic) | Null

Index Matches to: experiment samples

#### **Mix**

Indicates if this sample should be mixed while incubated, prior to starting the experiment.

Default Value: Automatic

Default Calculation: Automatically resolves to True if any Mix related options are set. Otherwise, resolves to False.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

#### **MixType**

Indicates the style of motion used to mix the sample, prior to starting the experiment.

Default Value: Automatic

Default Calculation: Automatically resolves based on the container of the sample and the Mix option.

Pattern Description: Roll, Vortex, Sonicate, Pipette, Invert, Stir, Shake, Homogenize, Swirl, Disrupt, or Nutate or Null.

Programmatic Pattern: (MixTypeP | Automatic) | Null

Index Matches to: experiment samples

#### **MixUntilDissolved**

Indicates if the mix should be continued up to the MaxIncubationTime or MaxNumberOfMixes (chosen according to the mix Type), in an attempt dissolve any solute. Any mixing/incubation will occur prior to starting the experiment.

Default Value: Automatic

Default Calculation: Automatically resolves to True if MaxIncubationTime or MaxNumberOfMixes is set.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

#### **MaxIncubationTime**

Maximum duration of time for which the samples will be mixed while incubated in an attempt to dissolve any solute, if the MixUntilDissolved option is chosen. This occurs prior to starting the experiment.

Default Value: Automatic

Default Calculation: Automatically resolves based on MixType, MixUntilDissolved, and the container of the given sample.

Pattern Description: Greater than or equal to 1 minute and less than or equal to 72 hours or Null.

Programmatic Pattern: (RangeP\[1\*Minute, $MaxExperimentTime\] | Automatic) | Null

Index Matches to: experiment samples

#### **IncubationInstrument**

The instrument used to perform the Mix and/or Incubation, prior to starting the experiment.

Default Value: Automatic

Default Calculation: Automatically resolves based on the options Mix, Temperature, MixType and container of the sample.

Pattern Description: An object of type or subtype Model\[Instrument, Roller\], Model\[Instrument, OverheadStirrer\], Model\[Instrument, Vortex\], Model\[Instrument, Shaker\], Model\[Instrument, BottleRoller\], Model\[Instrument, Roller\], Model\[Instrument, Sonicator\], Model\[Instrument, HeatBlock\], Model\[Instrument, Homogenizer\], Model\[Instrument, Disruptor\], Model\[Instrument, Nutator\], Model\[Instrument, Thermocycler\], Model\[Instrument, EnvironmentalChamber\], Model\[Instrument, Pipette\], Object\[Instrument, Roller\], Object\[Instrument, OverheadStirrer\], Object\[Instrument, Vortex\], Object\[Instrument, Shaker\], Object\[Instrument, BottleRoller\], Object\[Instrument, Roller\], Object\[Instrument, Sonicator\], Object\[Instrument, HeatBlock\], Object\[Instrument, Homogenizer\], Object\[Instrument, Disruptor\], Object\[Instrument, Nutator\], Object\[Instrument, Thermocycler\], Object\[Instrument, EnvironmentalChamber\], or Object\[Instrument, Pipette\] or Null.

Programmatic Pattern: (ObjectP\[Join\[MixInstrumentModels, MixInstrumentObjects\]\] | Automatic) | Null

Index Matches to: experiment samples

#### **AnnealingTime**

Minimum duration for which the SamplesIn should remain in the incubator allowing the system to settle to room temperature after the IncubationTime has passed but prior to starting the experiment.

Default Value: Automatic

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: (RangeP\[0\*Minute, $MaxExperimentTime\] | Automatic) | Null

Index Matches to: experiment samples

#### **IncubateAliquotContainer**

The desired type of container that should be used to prepare and house the incubation samples which should be used in lieu of the SamplesIn for the experiment.

Default Value: Automatic

Pattern Description: An object of type or subtype Model\[Container\] or {Index, Container} or Null.

Programmatic Pattern: ((ObjectP\[Model\[Container\]\] | {GreaterEqualP\[1, 1\] | (Automatic | Null), (ObjectP\[{Model\[Container\], Object\[Container\]}\] | \_String) | Automatic}) | Automatic) | Null

Index Matches to: experiment samples

#### **IncubateAliquotDestinationWell**

The desired position in the corresponding IncubateAliquotContainer in which the aliquot samples will be placed.

Default Value: Automatic

Default Calculation: Automatically resolves to A1 in containers with only one position. For plates, fills wells in the order provided by the function AllWells.

Pattern Description: Any well from A1 to H12 or Null.

Programmatic Pattern: (WellPositionP | Automatic) | Null

Index Matches to: experiment samples

#### **IncubateAliquot**

The amount of each sample that should be transferred from the SamplesIn into the IncubateAliquotContainer when performing an aliquot before incubation.

Default Value: Automatic

Default Calculation: Automatically set as the smaller between the current sample volume and the maximum volume of the destination container.

Pattern Description: All or greater than or equal to 1 microliter and less than or equal to 20 liters or Null.

Programmatic Pattern: ((RangeP\[1\*Microliter, 20\*Liter\] | All) | Automatic) | Null

Index Matches to: experiment samples

### Preparatory Centrifugation

#### **Centrifuge**

Indicates if the SamplesIn should be centrifuged prior to starting the experiment or any aliquoting. Sample Preparation occurs in the order of Incubation, Centrifugation, Filtration, and then Aliquoting (if specified).

Default Value: Automatic

Default Calculation: Resolves to True if any of the corresponding Centrifuge options are set. Otherwise, resolves to False.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

#### **CentrifugeInstrument**

The centrifuge that will be used to spin the provided samples prior to starting the experiment.

Default Value: Automatic

Pattern Description: An object of type or subtype Model\[Instrument, Centrifuge\] or Object\[Instrument, Centrifuge\] or Null.

Programmatic Pattern: (ObjectP\[{Model\[Instrument, Centrifuge\], Object\[Instrument, Centrifuge\]}\] | Automatic) | Null

Index Matches to: experiment samples

#### **CentrifugeIntensity**

The rotational speed or the force that will be applied to the samples by centrifugation prior to starting the experiment.

Default Value: Automatic

Pattern Description: Greater than 0 revolutions per minute or greater than 0 standard accelerations due to gravity on the surface of the earth or Null.

Programmatic Pattern: ((GreaterP\[0\*RPM\] | GreaterP\[0\*GravitationalAcceleration\]) | Automatic) | Null

Index Matches to: experiment samples

#### **CentrifugeTime**

The amount of time for which the SamplesIn should be centrifuged prior to starting the experiment.

Default Value: Automatic

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: (GreaterP\[0\*Minute\] | Automatic) | Null

Index Matches to: experiment samples

#### **CentrifugeTemperature**

The temperature at which the centrifuge chamber should be held while the samples are being centrifuged prior to starting the experiment.

Default Value: Automatic

Pattern Description: Ambient or greater than or equal to -10 degrees Celsius and less than or equal to 40 degrees Celsius or Null.

Programmatic Pattern: ((Ambient | RangeP\[-10\*Celsius, 40\*Celsius\]) | Automatic) | Null

Index Matches to: experiment samples

#### **CentrifugeAliquotContainer**

The desired type of container that should be used to prepare and house the centrifuge samples which should be used in lieu of the SamplesIn for the experiment.

Default Value: Automatic

Pattern Description: An object of type or subtype Model\[Container\] or {Index, Container} or Null.

Programmatic Pattern: ((ObjectP\[Model\[Container\]\] | {GreaterEqualP\[1, 1\] | (Automatic | Null), (ObjectP\[{Model\[Container\], Object\[Container\]}\] | \_String) | Automatic}) | Automatic) | Null

Index Matches to: experiment samples

#### **CentrifugeAliquotDestinationWell**

The desired position in the corresponding AliquotContainer in which the aliquot samples will be placed.

Default Value: Automatic

Default Calculation: Automatically resolves to A1 in containers with only one position. For plates, fills wells in the order provided by the function AllWells.

Pattern Description: Any well from A1 to H12 or Null.

Programmatic Pattern: (WellPositionP | Automatic) | Null

Index Matches to: experiment samples

#### **CentrifugeAliquot**

The amount of each sample that should be transferred from the SamplesIn into the CentrifugeAliquotContainer when performing an aliquot before centrifugation.

Default Value: Automatic

Default Calculation: Automatically set as the smaller between the current sample volume and the maximum volume of the destination container.

Pattern Description: All or greater than or equal to 1 microliter and less than or equal to 20 liters or Null.

Programmatic Pattern: ((RangeP\[1\*Microliter, 20\*Liter\] | All) | Automatic) | Null

Index Matches to: experiment samples

### Preparatory Filtering

#### **Filtration**

Indicates if the SamplesIn should be filter prior to starting the experiment or any aliquoting. Sample Preparation occurs in the order of Incubation, Centrifugation, Filtration, and then Aliquoting (if specified).

Default Value: Automatic

Default Calculation: Resolves to True if any of the corresponding Filter options are set. Otherwise, resolves to False.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

#### **FiltrationType**

The type of filtration method that should be used to perform the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to a filtration type appropriate for the volume of sample being filtered.

Pattern Description: PeristalticPump, Centrifuge, Vacuum, Syringe, or AirPressure or Null.

Programmatic Pattern: (FiltrationTypeP | Automatic) | Null

Index Matches to: experiment samples

#### **FilterInstrument**

The instrument that should be used to perform the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolved to an instrument appropriate for the filtration type.

Pattern Description: An object of type or subtype Model\[Instrument, FilterBlock\], Object\[Instrument, FilterBlock\], Model\[Instrument, PeristalticPump\], Object\[Instrument, PeristalticPump\], Model\[Instrument, VacuumPump\], Object\[Instrument, VacuumPump\], Model\[Instrument, Centrifuge\], Object\[Instrument, Centrifuge\], Model\[Instrument, SyringePump\], or Object\[Instrument, SyringePump\] or Null.

Programmatic Pattern: (ObjectP\[{Model\[Instrument, FilterBlock\], Object\[Instrument, FilterBlock\], Model\[Instrument, PeristalticPump\], Object\[Instrument, PeristalticPump\], Model\[Instrument, VacuumPump\], Object\[Instrument, VacuumPump\], Model\[Instrument, Centrifuge\], Object\[Instrument, Centrifuge\], Model\[Instrument, SyringePump\], Object\[Instrument, SyringePump\]}\] | Automatic) | Null

Index Matches to: experiment samples

#### **Filter**

The filter that should be used to remove impurities from the SamplesIn prior to starting the experiment.

Default Value: Automatic

Default Calculation: Will automatically resolve to a filter appropriate for the filtration type and instrument.

Pattern Description: An object of type or subtype Model\[Container, Plate, Filter\], Model\[Container, Vessel, Filter\], or Model\[Item, Filter\] or Null.

Programmatic Pattern: (ObjectP\[{Model\[Container, Plate, Filter\], Model\[Container, Vessel, Filter\], Model\[Item, Filter\]}\] | Automatic) | Null

Index Matches to: experiment samples

#### **FilterMaterial**

The membrane material of the filter that should be used to remove impurities from the SamplesIn prior to starting the experiment.

Default Value: Automatic

Default Calculation: Resolves to an appropriate filter material for the given sample is Filtration is set to True.

Pattern Description: Cellulose, Cotton, Polyethylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

Programmatic Pattern: (FilterMembraneMaterialP | Automatic) | Null

Index Matches to: experiment samples

#### **PrefilterMaterial**

The material from which the prefilter filtration membrane should be made of to remove impurities from the SamplesIn prior to starting the experiment.

Default Value: Automatic

Default Calculation: By default, no prefiltration is performed on samples, even when Filter->True.

Pattern Description: Cellulose, Cotton, Polyethylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

Programmatic Pattern: (FilterMembraneMaterialP | Automatic) | Null

Index Matches to: experiment samples

#### **FilterPoreSize**

The pore size of the filter that should be used when removing impurities from the SamplesIn prior to starting the experiment.

Default Value: Automatic

Default Calculation: Resolves to an appropriate filter pore size for the given sample is Filtration is set to True.

Pattern Description: 0.008 micrometers, 0.1 micrometers, 0.22 micrometers, 0.45 micrometers, 1. micrometer, 1.1 micrometers, 2.5 micrometers, 6. micrometers, 20. micrometers, 30. micrometers, or 100. micrometers or Null.

Programmatic Pattern: (FilterSizeP | Automatic) | Null

Index Matches to: experiment samples

#### **PrefilterPoreSize**

The pore size of the filter; all particles larger than this should be removed during the filtration.

Default Value: Automatic

Default Calculation: By default, no prefiltration is performed on samples, even when Filter->True.

Pattern Description: 0.008 micrometers, 0.1 micrometers, 0.22 micrometers, 0.45 micrometers, 1. micrometer, 1.1 micrometers, 2.5 micrometers, 6. micrometers, 20. micrometers, 30. micrometers, or 100. micrometers or Null.

Programmatic Pattern: (FilterSizeP | Automatic) | Null

Index Matches to: experiment samples

#### **FilterSyringe**

The syringe used to force that sample through a filter.

Default Value: Automatic

Default Calculation: Resolves to an syringe appropriate to the volume of sample being filtered, if Filtration is set to True.

Pattern Description: An object of type or subtype Model\[Container, Syringe\] or Object\[Container, Syringe\] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP\[{Model\[Container, Syringe\], Object\[Container, Syringe\]}\] | \_String) | Automatic) | Null

Index Matches to: experiment samples

#### **FilterHousing**

The filter housing that should be used to hold the filter membrane when filtration is performed using a standalone filter membrane.

Default Value: Automatic

Default Calculation: Resolve to an housing capable of holding the size of the membrane being used, if filter with Membrane FilterType is being used and Filtration is set to True.

Pattern Description: An object of type or subtype Model\[Instrument, FilterHousing\], Object\[Instrument, FilterHousing\], Model\[Instrument, FilterBlock\], or Object\[Instrument, FilterBlock\] or Null.

Programmatic Pattern: (ObjectP\[{Model\[Instrument, FilterHousing\], Object\[Instrument, FilterHousing\], Model\[Instrument, FilterBlock\], Object\[Instrument, FilterBlock\]}\] | Automatic) | Null

Index Matches to: experiment samples

#### **FilterIntensity**

The rotational speed or force at which the samples will be centrifuged during filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to 2000 GravitationalAcceleration if FiltrationType is Centrifuge and Filtration is True.

Pattern Description: Greater than 0 revolutions per minute or greater than 0 standard accelerations due to gravity on the surface of the earth or Null.

Programmatic Pattern: ((GreaterP\[0\*RPM\] | GreaterP\[0\*GravitationalAcceleration\]) | Automatic) | Null

Index Matches to: experiment samples

#### **FilterTime**

The amount of time for which the samples will be centrifuged during filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to 5 Minute if FiltrationType is Centrifuge and Filtration is True.

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: (GreaterP\[0\*Minute\] | Automatic) | Null

Index Matches to: experiment samples

#### **FilterTemperature**

The temperature at which the centrifuge chamber will be held while the samples are being centrifuged during filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to 22 Celsius if FiltrationType is Centrifuge and Filtration is True.

Pattern Description: Greater than or equal to 4 degrees Celsius or Null.

Programmatic Pattern: ((Alternatives\[GreaterEqualP\[4\*Celsius\]\]) | Automatic) | Null

Index Matches to: experiment samples

#### **FilterContainerOut**

The desired container filtered samples should be produced in or transferred into by the end of filtration, with indices indicating grouping of samples in the same plates, if desired.

Default Value: Automatic

Default Calculation: Automatically set as the PreferredContainer for the Volume of the sample. For plates, attempts to fill all wells of a single plate with the same model before using another one.

Pattern Description: An object of type or subtype Model\[Container\] or Object\[Container\] or a prepared sample or {Index, Container} or Null.

Programmatic Pattern: (((ObjectP\[{Model\[Container\], Object\[Container\]}\] | \_String) | {GreaterEqualP\[1, 1\] | Automatic, (ObjectP\[{Model\[Container\], Object\[Container\]}\] | \_String) | Automatic}) | Automatic) | Null

Index Matches to: experiment samples

#### **FilterAliquotDestinationWell**

The desired position in the corresponding AliquotContainer in which the aliquot samples will be placed.

Default Value: Automatic

Default Calculation: Automatically resolves to A1 in containers with only one position. For plates, fills wells in the order provided by the function AllWells.

Pattern Description: Any well from A1 to H12 or Null.

Programmatic Pattern: (WellPositionP | Automatic) | Null

Index Matches to: experiment samples

#### **FilterAliquotContainer**

The desired type of container that should be used to prepare and house the filter samples which should be used in lieu of the SamplesIn for the experiment.

Default Value: Automatic

Pattern Description: An object of type or subtype Model\[Container\] or {Index, Container} or Null.

Programmatic Pattern: ((ObjectP\[Model\[Container\]\] | {GreaterEqualP\[1, 1\] | (Automatic | Null), (ObjectP\[{Model\[Container\], Object\[Container\]}\] | \_String) | Automatic}) | Automatic) | Null

Index Matches to: experiment samples

#### **FilterAliquot**

The amount of each sample that should be transferred from the SamplesIn into the FilterAliquotContainer when performing an aliquot before filtration.

Default Value: Automatic

Default Calculation: Automatically set as the smaller between the current sample volume and the maximum volume of the destination container.

Pattern Description: All or greater than or equal to 1 microliter and less than or equal to 20 liters or Null.

Programmatic Pattern: ((RangeP\[1\*Microliter, 20\*Liter\] | All) | Automatic) | Null

Index Matches to: experiment samples

#### **FilterSterile**

Indicates if the filtration of the samples should be done in a sterile environment.

Default Value: Automatic

Default Calculation: Resolve to False if Filtration is indicated. If sterile filtration is desired, this option must manually be set to True.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

### Aliquoting

#### **Aliquot**

Indicates if aliquots should be taken from the SamplesIn and transferred into new AliquotSamples used in lieu of the SamplesIn for the experiment. Note that if NumberOfReplicates is specified this indicates that the input samples will also be aliquoted that number of times. Note that Aliquoting (if specified) occurs after any Sample Preparation (if specified).

Default Value: Automatic

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

#### **AliquotAmount**

The amount of a sample that should be transferred from the input samples into aliquots.

Default Value: Automatic

Default Calculation: Automatically set as the smaller between the current sample volume and the maximum volume of the destination container if a liquid, or the current Mass or Count if a solid or counted item, respectively.

Pattern Description: All or Count or Count or Mass or Volume or Null.

Programmatic Pattern: ((RangeP\[1\*Microliter, 20\*Liter\] | RangeP\[1\*Milligram, 20\*Kilogram\] | GreaterP\[0\*Unit, 1\*Unit\] | GreaterP\[0., 1.\] | All) | Automatic) | Null

Index Matches to: experiment samples

#### **TargetConcentration**

The desired final concentration of analyte in the AliquotSamples after dilution of aliquots of SamplesIn with the ConcentratedBuffer and BufferDiluent which should be used in lieu of the SamplesIn for the experiment.

Default Value: Automatic

Default Calculation: Automatically calculated based on aliquot and buffer volumes.

Pattern Description: Greater than 0 molar or greater than 0 grams per liter or Null.

Programmatic Pattern: ((GreaterP\[0\*Molar\] | GreaterP\[(0\*Gram)/Liter\]) | Automatic) | Null

Index Matches to: experiment samples

#### **TargetConcentrationAnalyte**

The substance whose final concentration is attained with the TargetConcentration option.

Default Value: Automatic

Default Calculation: Automatically set to the first value in the Analytes field of the input sample, or, if not populated, to the first analyte in the Composition field of the input sample, or if none exist, the first identity model of any kind in the Composition field.

Pattern Description: An object of type or subtype Model\[Molecule\], Model\[Molecule, cDNA\], Model\[Molecule, Oligomer\], Model\[Molecule, Transcript\], Model\[Molecule, Protein\], Model\[Molecule, Protein, Antibody\], Model\[Molecule, Carbohydrate\], Model\[Molecule, Polymer\], Model\[Resin\], Model\[Resin, SolidPhaseSupport\], Model\[Lysate\], Model\[ProprietaryFormulation\], Model\[Virus\], Model\[Cell\], Model\[Cell, Mammalian\], Model\[Cell, Bacteria\], Model\[Cell, Yeast\], Model\[Tissue\], Model\[Material\], or Model\[Species\] or Null.

Programmatic Pattern: (ObjectP\[IdentityModelTypes\] | Automatic) | Null

Index Matches to: experiment samples

#### **AssayVolume**

The desired total volume of the aliquoted sample plus dilution buffer.

Default Value: Automatic

Default Calculation: Automatically determined based on Volume and TargetConcentration option values.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 20 liters or Null.

Programmatic Pattern: (RangeP\[1\*Microliter, 20\*Liter\] | Automatic) | Null

Index Matches to: experiment samples

#### **ConcentratedBuffer**

The concentrated buffer which should be diluted by the BufferDilutionFactor in the final solution (i.e., the combination of the sample, ConcentratedBuffer, and BufferDiluent). The ConcentratedBuffer and BufferDiluent will be combined and then mixed with the sample, where the combined volume of these buffers is the difference between the AliquotAmount and the total AssayVolume.

Default Value: Automatic

Pattern Description: An object of type or subtype Model\[Sample\] or Object\[Sample\] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP\[{Model\[Sample\], Object\[Sample\]}\] | \_String) | Automatic) | Null

Index Matches to: experiment samples

#### **BufferDilutionFactor**

The dilution factor by which the concentrated buffer should be diluted in the final solution (i.e., the combination of the sample, ConcentratedBuffer, and BufferDiluent). The ConcentratedBuffer and BufferDiluent will be combined and then mixed with the sample, where the combined volume of these buffers is the difference between the AliquotAmount and the total AssayVolume.

Default Value: Automatic

Default Calculation: If ConcentratedBuffer is specified, automatically set to the ConcentratedBufferDilutionFactor of that sample; otherwise, set to Null.

Pattern Description: Greater than or equal to 1 or Null.

Programmatic Pattern: (GreaterEqualP\[1\] | Automatic) | Null

Index Matches to: experiment samples

#### **BufferDiluent**

The buffer used to dilute the aliquot sample such that ConcentratedBuffer is diluted by BufferDilutionFactor in the final solution. The ConcentratedBuffer and BufferDiluent will be combined and then mixed with the sample, where the combined volume of these buffers is the difference between the AliquotAmount and the total AssayVolume.

Default Value: Automatic

Default Calculation: Automatically resolves to Model\[Sample, "Milli-Q water"\] if ConcentratedBuffer is specified; otherwise, resolves to Null.

Pattern Description: An object of type or subtype Model\[Sample\] or Object\[Sample\] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP\[{Model\[Sample\], Object\[Sample\]}\] | \_String) | Automatic) | Null

Index Matches to: experiment samples

#### **AssayBuffer**

The buffer that should be added to any aliquots requiring dilution, where the volume of this buffer added is the difference between the AliquotAmount and the total AssayVolume.

Default Value: Automatic

Default Calculation: Automatically resolves to Model\[Sample, "Milli-Q water"\] if ConcentratedBuffer is not specified; otherwise, resolves to Null.

Pattern Description: An object of type or subtype Model\[Sample\] or Object\[Sample\] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP\[{Model\[Sample\], Object\[Sample\]}\] | \_String) | Automatic) | Null

Index Matches to: experiment samples

#### **AliquotSampleStorageCondition**

The non-default conditions under which any aliquot samples generated by this experiment should be stored after the protocol is completed.

Default Value: Automatic

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, BacteriaIncubation, MammalianIncubation, TissueCultureCellsIncubation, MicrobialCellsIncubation, MicrobialCellsShakingIncubation, YeastCellsIncubation, YeastCellsShakingIncubation, ViralIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: ((SampleStorageTypeP | Disposal) | Automatic) | Null

Index Matches to: experiment samples

#### **DestinationWell**

The desired position in the corresponding AliquotContainer in which the aliquot samples will be placed.

Default Value: Automatic

Default Calculation: Automatically resolves to A1 in containers with only one position. For plates, fills wells in the order provided by the function AllWells.

Pattern Description: Any well from A1 to H12 or list of one or more any well from A1 to H12 or any well from A1 to H12 entries or Null.

Programmatic Pattern: ((WellPositionP | {((Automatic | Null) | WellPositionP)..}) | Automatic) | Null

#### **AliquotContainer**

The desired type of container that should be used to prepare and house the aliquot samples, with indices indicating grouping of samples in the same plates, if desired. This option will resolve to be the length of the SamplesIn \* NumberOfReplicates.

Default Value: Automatic

Default Calculation: Automatically set as the PreferredContainer for the AssayVolume of the sample. For plates, attempts to fill all wells of a single plate with the same model before aliquoting into the next.

Pattern Description: An object of type or subtype Model\[Container\] or Object\[Container\] or a prepared sample or Automatic or Null or {Index, Container} or list of one or more an object of type or subtype Model\[Container\] or Object\[Container\] or a prepared sample or Automatic or Null entries or list of one or more Automatic or Null or {Index, Container} entries or Null.

Programmatic Pattern: (((ObjectP\[{Model\[Container\], Object\[Container\]}\] | \_String) | (Automatic | Null) | {GreaterEqualP\[1, 1\] | (Automatic | Null), (ObjectP\[{Model\[Container\], Object\[Container\]}\] | \_String) | (Automatic | Null)} | {((ObjectP\[{Model\[Container\], Object\[Container\]}\] | \_String) | (Automatic | Null))..} | {({GreaterEqualP\[1, 1\] | (Automatic | Null), (ObjectP\[{Model\[Container\], Object\[Container\]}\] | \_String) | (Automatic | Null)} | (Automatic | Null))..}) | Automatic) | Null

#### **AliquotPreparation**

Indicates the desired scale at which liquid handling used to generate aliquots will occur.

Default Value: Automatic

Default Calculation: Automatic resolution will occur based on manipulation volumes and container types.

Pattern Description: Manual or Robotic or Null.

Programmatic Pattern: (PreparationMethodP | Automatic) | Null

#### **ConsolidateAliquots**

Indicates if identical aliquots should be prepared in the same container/position.

Default Value: Automatic

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Protocol Options
================

### Organizational Information

#### **Template**

A template protocol whose methodology should be reproduced in running this experiment. Option values will be inherited from the template protocol, but can be individually overridden by directly specifying values for those options to this Experiment function.

Default Value: Null

Pattern Description: An object of type or subtype Object\[Protocol\] or an object of type or subtype of Object\[Protocol\] with UnresolvedOptions, ResolvedOptions specified or Null.

Programmatic Pattern: (ObjectP\[Object\[Protocol\]\] | FieldReferenceP\[Object\[Protocol\], {UnresolvedOptions, ResolvedOptions}\]) | Null

#### **Name**

A object name which should be used to refer to the output object in lieu of an automatically generated ID number.

Default Value: Null

Pattern Description: A string or Null.

Programmatic Pattern: \_String | Null

### Post Experiment

#### **MeasureWeight**

Indicates if any solid samples that are modified in the course of the experiment should have their weights measured and updated after running the experiment. Please note that public samples are weighed regardless of the value of this option.

Default Value: Automatic

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

#### **MeasureVolume**

Indicates if any liquid samples that are modified in the course of the experiment should have their volumes measured and updated after running the experiment. Please note that public samples are volume measured regardless of the value of this option.

Default Value: Automatic

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

#### **ImageSample**

Indicates if any samples that are modified in the course of the experiment should be freshly imaged after running the experiment. Please note that public samples are imaged regardless of the value of this option.

Default Value: Automatic

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Example Calls
=============

### Basics

High performance liquid chromatography (HPLC) separates sample mixtures into analyzable molecular constituents by injection into flowing liquid that passes through a retentive column:

![](Files/ExperimentLCMS.en/I_14.png)

### MassAnalyzer

Use MassAnalyzer option to select TripleQuadruploe as the mass analyzer

![](Files/ExperimentLCMS.en/I_15.png)

### Separation Mode and Gradient

More specific buffers and gradient profiles can also be articulated. For example:

![](Files/ExperimentLCMS.en/I_16.png)

A full gradient table can be specified:

![](Files/ExperimentLCMS.en/I_17.png)

### Ionization

The polarity of the ions analyzed can be set along with the desired reference solution for the sample masses:

![](Files/ExperimentLCMS.en/I_18.png)

Specific settings for electrospray ionization source can be controlled in order to maximize ionization capability:

![](Files/ExperimentLCMS.en/I_19.png)

### Acquisition Windows and Modes

Different acquisition modes can be specified within different time periods for the same chromatogram. Here, for all of the samples, during the time period from 2 minutes to 5 minutes, an MS1FullScan acquisition is employed (no fragmentation; measure intact ions). From 7 minutes to 9, a data dependent acquisition is performed (see the appropriate section above):

![](Files/ExperimentLCMS.en/I_20.png)

Similarly, different fragmentation instructions can be specified for different time periods:

![](Files/ExperimentLCMS.en/I_21.png)

### Multiple Reaction Monitoring

Specified MassAnalyzer, AcquisitionMode, MassSelection and FragmentMassSelection to conduct multiple reaction monitoring analysis by using QTRAP 6500:

![](Files/ExperimentLCMS.en/I_22.png)

Specified MassAnalyzer, AcquisitionMode and MultipleReactionMonitoringAssays to conduct multiple reaction monitoring analysis by using QTRAP 6500:

![](Files/ExperimentLCMS.en/I_23.png)

### Data Dependent Acquisition

In data dependent acquisition, the measurement is split into cycles (see the figure above). In the first part of the cycle, the intact ions (no fragmentations) are surveyed and considered for fragmentation analysis:

![](Files/ExperimentLCMS.en/I_24.png)

A threshold can be specified on whether to consider an intact ion for fragmentation analysis. Likewise, a limit can be placed so that a highly abundant ion is not overly analyzed:

![](Files/ExperimentLCMS.en/I_25.png)

Various m/z can be excluded from the acquisition program:

![](Files/ExperimentLCMS.en/I_26.png)

Masses can be prioritized for fragmentation as they surface during the surveys:

![](Files/ExperimentLCMS.en/I_27.png)

Masses can be prioritized for fragmentation as they surface during the surveys:

![](Files/ExperimentLCMS.en/I_27.png)

Redundant isotopes can excluded from acquisition surveys:

![](Files/ExperimentLCMS.en/I_29.png)

Redundant charge states can excluded from acquisition surveys:

![](Files/ExperimentLCMS.en/I_30.png)

### Standards and Blanks

ExperimentLCMS can be used to quantify analytes in a sample, in which case, a Standard sample is employed to serve as reference. A standard can be submitted before and after the injection sequence of the samples simply by running:

![](Files/ExperimentLCMS.en/I_31.png)

Likewise, a Blank sample can be used to see if there is any background from the injection process. To run a blank to occur between every 5 samples, use the following command:

![](Files/ExperimentLCMS.en/I_32.png)

### PhotoDiodeArray detection

PhotoDiodeArray detection involves passes light across a range of wavelengths and measures how much light is absorbed for each even wavelength:

![](Files/ExperimentLCMS.en/I_33.png)

### Injection Table

In addition to specifying frequencies of running standards and blanks, now the injection sequence of samples, standards, blanks, and column primes/flushes can be explicitly articulated as well. In this case, an additional column flush is specified after the injection of the second sample:

![](Files/ExperimentLCMS.en/I_34.png)

![](Files/ExperimentLCMS.en/I_35.png)

Preferred Input Containers
==========================

The autosampler can take 2mL deep well plates.



The autosampler can take normal vials routinely used in HPLC analysis.



Data Processing
===============

The data can be viewed by PlotChromatographyMassSpectra