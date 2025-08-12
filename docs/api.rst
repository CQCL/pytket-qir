API documentation
~~~~~~~~~~~~~~~~~

.. automodule:: pytket.qir
.. automodule:: pytket.qir._metadata
.. automodule:: pytket.qir.conversion
.. automodule:: pytket.qir.conversion.api

    .. autofunction:: pytket_to_qir
    
    .. autoclass:: QIRFormat

    .. autoclass:: QIRProfile

    .. autoexception:: ClassicalRegisterWidthError

    .. autofunction:: check_circuit

.. automodule:: pytket.qir.conversion.qirgenerator

    .. autoclass:: AbstractQirGenerator

        .. automethod:: circuit_to_module
        .. automethod:: command_to_module
        .. automethod:: record_output
        .. automethod:: subcircuit_to_module
        .. automethod:: conv_BarrierOp
        .. automethod:: conv_CopyBitsOp
        .. automethod:: conv_RangePredicateOp
        .. automethod:: conv_SetBitsOp
        .. automethod:: conv_WASMOp
        .. automethod:: conv_ZZPhase
        .. automethod:: conv_RNGJobOp
        .. automethod:: conv_RNGJobOpR
        .. automethod:: conv_clexprop
        .. automethod:: conv_conditional
        .. automethod:: conv_measure
        .. automethod:: conv_other
        .. automethod:: conv_phasedx
        .. automethod:: conv_tk2
        .. automethod:: conv_zzmax
        .. automethod:: get_azure_sar
        .. automethod:: get_ssa_vars
        .. automethod:: get_wasm_sar
        .. automethod:: set_ssa_vars

.. automodule:: pytket.qir.conversion.baseprofileqirgenerator

    .. autoclass:: BaseProfileQirGenerator

        .. automethod:: record_output
        .. automethod:: conv_conditional
        .. automethod:: conv_measure
        .. automethod:: get_ssa_list
        .. automethod:: get_ssa_vars
        .. automethod:: set_ssa_vars

.. automodule:: pytket.qir.conversion.profileqirgenerator

    .. autoclass:: AdaptiveProfileQirGenerator

        .. automethod:: record_output
        .. automethod:: conv_conditional
        .. automethod:: conv_measure
        .. automethod:: get_ssa_list
        .. automethod:: get_ssa_vars
        .. automethod:: set_ssa_vars

.. automodule:: pytket.qir.conversion.pytketqirgenerator

    .. autoclass:: PytketQirGenerator

        .. automethod:: record_output
        .. automethod:: conv_conditional
        .. automethod:: conv_measure
        .. automethod:: get_ssa_vars
        .. automethod:: set_ssa_vars

.. automodule:: pytket.qir.conversion.azurebaseprofileqirgenerator

    .. autoclass:: AzureBaseProfileQirGenerator

        .. automethod:: record_output
        .. automethod:: conv_measure

.. automodule:: pytket.qir.conversion.azureprofileqirgenerator

    .. autoclass:: AzureAdaptiveProfileQirGenerator

        .. automethod:: record_output
        .. automethod:: conv_measure

.. automodule:: pytket.qir.conversion.module

    .. autoclass:: tketqirModule

.. automodule:: pytket.qir.conversion.gatesets

    .. autoclass:: QirGate
    .. autoclass:: CustomQirGate
    .. autoclass:: CustomGateSet
    .. autoclass:: FuncName
    .. autoclass:: FuncNat
    .. autoclass:: FuncSpec
