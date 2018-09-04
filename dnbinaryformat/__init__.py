import hexdump
import vstruct
from vstruct.primitives import *






RecordTypeEnumerator = v_enum()

RecordTypeEnumerator.SerializedStreamHeader = 0
RecordTypeEnumerator.ClassWithId = 1
RecordTypeEnumerator.SystemClassWithMembers = 2
RecordTypeEnumerator.ClassWithMembers = 3
RecordTypeEnumerator.SystemClassWithMembersAndTypes = 4
RecordTypeEnumerator.ClassWithMembersAndTypes = 5
RecordTypeEnumerator.BinaryObjectString = 6
RecordTypeEnumerator.BinaryArray = 7
RecordTypeEnumerator.MemberPrimitiveTyped = 8
RecordTypeEnumerator.MemberReference = 9
RecordTypeEnumerator.ObjectNull = 10
RecordTypeEnumerator.MessageEnd = 11
RecordTypeEnumerator.BinaryLibrary = 12
RecordTypeEnumerator.ObjectNullMultiple256 = 13
RecordTypeEnumerator.ObjectNullMultiple = 14
RecordTypeEnumerator.ArraySinglePrimitive = 15
RecordTypeEnumerator.ArraySingleObject = 16
RecordTypeEnumerator.ArraySingleString = 17
RecordTypeEnumerator.MethodCall = 21
RecordTypeEnumerator.MethodReturn = 22


BinaryTypeEnumerator = v_enum()
BinaryTypeEnumerator.Primitive = 0
BinaryTypeEnumerator.String = 1
BinaryTypeEnumerator.Object = 2
BinaryTypeEnumerator.SystemClass = 3
BinaryTypeEnumerator.Class = 4
BinaryTypeEnumerator.ObjectArray = 5
BinaryTypeEnumerator.StringArray = 6
BinaryTypeEnumerator.PrimitiveArray = 7

PrimitiveTypeEnumeration = v_enum()
PrimitiveTypeEnumeration.Boolean = 1
PrimitiveTypeEnumeration.Byte = 2
PrimitiveTypeEnumeration.Char = 3
PrimitiveTypeEnumeration.Unused = 4
PrimitiveTypeEnumeration.Decimal = 5
PrimitiveTypeEnumeration.Double = 6
PrimitiveTypeEnumeration.Int16 = 7
PrimitiveTypeEnumeration.Int32 = 8
PrimitiveTypeEnumeration.Int64 = 9
PrimitiveTypeEnumeration.SByte = 10
PrimitiveTypeEnumeration.Single = 11
PrimitiveTypeEnumeration.TimeSpan = 12
PrimitiveTypeEnumeration.DateTime = 13
PrimitiveTypeEnumeration.UInt16 = 14
PrimitiveTypeEnumeration.UInt32 = 15
PrimitiveTypeEnumeration.UInt64 = 16
PrimitiveTypeEnumeration.Null = 17
PrimitiveTypeEnumeration.String = 18

MessageFlags = v_enum()
MessageFlags.NoArgs = 0x00000001
MessageFlags.ArgsInline = 0x00000002
MessageFlags.ArgsIsArray = 0x00000004
MessageFlags.ArgsInArray = 0x00000008
MessageFlags.NoContext = 0x00000010
MessageFlags.ContextInline = 0x00000020
MessageFlags.ContextInArray = 0x00000040
MessageFlags.MethodSignatureInArray = 0x00000080
MessageFlags.PropertiesInArray = 0x00000100
MessageFlags.NoReturnValue = 0x00000200
MessageFlags.ReturnValueVoid = 0x00000400
MessageFlags.ReturnValueInline = 0x00000800
MessageFlags.ReturnValueInArray = 0x00001000
MessageFlags.ExceptionInArray = 0x00002000
MessageFlags.GenericMethod = 0x00008000


class LengthPrefixedString(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.Length = 0
        self.Value = ''

    def vsParse(self, bytez, offset=0, fast=False):
        length = bytez[offset + 0] & 0b01111111
        if bytez[offset + 0] & 0b10000000:
            # TODO: need an example of this to test against
            # don't want to code blind.
            raise NotImplementedError()

        value = bytez[offset + 1:offset + 1 + length].decode('utf-8')

        self.Length = length
        self.Value = value
        return offset + length + 1

    def __repr__(self):
        return 'LengthPrefixedString: %s' % (self.Value)

    def __len__(self):
        return self.Length + 1


class ClassTypeInfo(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.TypeName = LengthPrefixedString()
        self.LibraryId = v_int32()


class SerializationHeaderRecord(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.RecordTypeEnum = v_uint8(enum=RecordTypeEnumerator)
        self.RootId = v_int32()
        self.HeaderId = v_int32()
        self.MajorVersion = v_int32()
        self.MinorVersion = v_int32()


class ValueWithCode(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        raise NotImplementedError()


class StringWithCode(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.PrimitiveTypeEnum = v_uint8(enum=PrimitiveTypeEnumeration)
        self.StringValue = LengthPrefixedString()

    def pcb_PrimitiveTypeEnum(self):
        assert self.PrimitiveTypeEnum == PrimitiveTypeEnumeration.String


class ArrayOfValueWithCode(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.Length = v_int32()
        self.ListOfValueWithCode = vstruct.VArray()

    def pcb_Length(self):
        for i in range(self.Length):
            self.ListOfValueWithCode.vsAddElement(ValueWithCode())


class BinaryMethodCall(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.RecordTypeEnum = v_uint8(enum=RecordTypeEnumeration)
        self.MessageEnum = v_uint32()  # bitmask=MessageFlags
        self.MethodName = StringValueWithCode()
        self.TypeName = StringValueWithCode()
        raise NotImplementedError()
        # if self.MessageEnum & ContextInline
        self.CallContext = None  # StringValueWithCode
        # if self.MessageEnum & ArgsInline
        self.Args = None  # ArrayOfValueWithCode()


    def pcb_RecordTypeEnum(self):
        assert self.RecordTypeEnum == RecordTypeEnumeration.MethodCall



# ...


class ClassInfo(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.ObjectId = v_int32()
        self.Name = LengthPrefixedString()
        self.MemberCount = v_int32()
        self.MemberNames = vstruct.VArray()

    def pcb_MemberCount(self):
        for i in range(self.MemberCount):
            self.MemberNames.vsAddElement(LengthPrefixedString())


class MemberTypeInfo(vstruct.VStruct):
    def __init__(self, member_count=0):
        vstruct.VStruct.__init__(self)
        self.member_count = member_count
        # not precisely correct: should be v_int8, but this has no `enum` kwarg at the moment
        self.BinaryTypeEnums = vstruct.VArray([v_uint8(enum=BinaryTypeEnumerator)] * member_count)
        self.AdditionalInfos = vstruct.VArray()

    def set_member_count(self, member_count):
        if self.member_count != 0:
            raise ValueError('cannot set member count after it is initialized')

        for i in range(member_count):
            self.BinaryTypeEnums.vsAddElement(v_uint8(enum=BinaryTypeEnumerator))

    def pcb_BinaryTypeEnums(self):
        for (_, entry) in self.BinaryTypeEnums:
            if int(entry) == BinaryTypeEnumerator.Primitive:
                self.AdditionalInfos.vsAddElement(v_uint8(enum=PrimitiveTypeEnumeration))
            elif int(entry) == BinaryTypeEnumerator.SystemClass:
                self.AdditionalInfos.vsAddElement(LengthPrefixedString())
            elif int(entry) == BinaryTypeEnumerator.Class:
                self.AdditionalInfos.vsAddElement(ClassTypeInfo())
            elif int(entry) == BinaryTypeEnumerator.PrimitiveArray:
                self.AdditionalInfos.vsAddElement(v_uint8(enum=PrimitiveTypeEnumeration))
            else:
                continue


class SystemClassWithMembersAndTypes(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.RecordTypeEnum = v_uint8(enum=RecordTypeEnumerator)
        self.ClassInfo = ClassInfo()
        self.MemberTypeInfo = MemberTypeInfo(member_count=0)

    def pcb_RecordTypeEnum(self):
        assert self.RecordTypeEnum == RecordTypeEnumerator.SystemClassWithMembersAndTypes

    def pcb_ClassInfo(self):
        self.MemberTypeInfo.set_member_count(self.ClassInfo.MemberCount)


class MemberReference(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.RecordTypeEnum = v_uint8(enum=RecordTypeEnumerator)
        self.IdRef = v_int32()

    def pcb_RecordTypeEnum(self):
        assert self.RecordTypeEnum == RecordTypeEnumerator.MemberReference


class BinaryObjectString(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.RecordTypeEnum = v_uint8(enum=RecordTypeEnumerator)
        self.ObjectId = v_int32()
        self.Value = LengthPrefixedString()

    def pcb_RecordTypeEnum(self):
        assert self.RecordTypeEnum == RecordTypeEnumerator.BinaryObjectString


class ObjectNull(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.RecordTypeEnum = v_uint8(enum=RecordTypeEnumerator)

    def pcb_RecordTypeEnum(self):
        assert self.RecordTypeEnum == RecordTypeEnumerator.ObjectNull


class MemberPrimitiveTyped(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.RecordTypeEnum = v_uint8(enum=RecordTypeEnumerator)
        self.PrimitiveTypeEnum = v_uint8(enum=PrimitiveTypeEnumeration)
        # self.Value = *
        self._eof = v_bytes()

    def pcb_RecordTypeEnum(self):
        assert self.RecordTypeEnum == RecordTypeEnumerator.MemberPrimitiveTyped

    def pcb_PrimitiveTypeEnum(self):
        if int(self.PrimitiveTypeEnum) == 0x0:
            # enum instance is not documented. seems to be | 00 00 | in practice?
            self.vsInsertField('Value', v_uint16(), '_eof')
        else:
            # trivial to implement, once we see sample data.
            raise NotImplementedError()


class ClassWithId(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.RecordTypeEnum = v_uint8(enum=RecordTypeEnumerator)
        self.ObjectId = v_int32()
        self.MetadataId = v_int32()

    def pcb_RecordTypeEnum(self):
        assert self.RecordTypeEnum == RecordTypeEnumerator.ClassWithId


class ArrayInfo(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.ObjectId = v_int32()
        self.Length = v_int32()


class ArraySinglePrimitive(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.RecordTypeEnum = v_uint8(enum=RecordTypeEnumerator)
        self.ArrayInfo = ArrayInfo()
        self.PrimitiveTypeEnum = v_uint8(enum=PrimitiveTypeEnumeration)
        # self.Value = *
        self._eof = v_bytes()

    def pcb_RecordTypeEnum(self):
        assert self.RecordTypeEnum == RecordTypeEnumerator.ArraySinglePrimitive

    def pcb_PrimitiveTypeEnum(self):
        if self.PrimitiveTypeEnum == PrimitiveTypeEnumeration.Byte:
            self.vsInsertField('Value', v_bytes(size=self.ArrayInfo.Length), '_eof')
        else:
            # trivial to implement, once we see sample data
            raise NotImplementedError()


class MessageEnd(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.RecordTypeEnum = v_uint8(enum=RecordTypeEnumerator)

    def pcb_RecordTypeEnum(self):
        assert self.RecordTypeEnum == RecordTypeEnumerator.MessageEnd


class SerializedData(vstruct.VArray):
    def __init__(self):
        vstruct.VArray.__init__(self)
        self.count = 0

    def vsParse(self, bytez, offset=0, fast=False):
        while len(bytez) > offset:
            record_type = bytez[offset]

            if record_type == RecordTypeEnumerator.SerializedStreamHeader:
                record = SerializationHeaderRecord()
            elif record_type == RecordTypeEnumerator.SystemClassWithMembersAndTypes:
                record = SystemClassWithMembersAndTypes()
            elif record_type == RecordTypeEnumerator.ClassWithId:
                record = ClassWithId()
            elif record_type == RecordTypeEnumerator.MemberReference:
                record = MemberReference()
            elif record_type == RecordTypeEnumerator.BinaryObjectString:
                record = BinaryObjectString()
            elif record_type == RecordTypeEnumerator.ObjectNull:
                record = ObjectNull()
            elif record_type == RecordTypeEnumerator.MemberPrimitiveTyped:
                record = MemberPrimitiveTyped()
            elif record_type == RecordTypeEnumerator.ArraySinglePrimitive:
                record = ArraySinglePrimitive()
            elif record_type == RecordTypeEnumerator.MessageEnd:
                record = MessageEnd()
            else:
                # these other options are documented, just not implemented here yet
                raise NotImplementedError()

            record.vsParse(bytez, offset)
            self.vsAddElement(record)
            offset += len(record)
            self.count += 1

            if record_type == RecordTypeEnumerator.MessageEnd:
                break

        return offset


def deserialize(buf):
    d = SerializedData()
    d.vsParse(buf)
    return d
