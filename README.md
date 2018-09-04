# python-dotnet-binaryformat
Pure Python parser for data encoded by .NET's BinaryFormatter


## scripts

### extract_pe.py

Searches for embedded byte arrays that begin with `MZ` and write them to a file named after their MD5 hash.


Example::

```
λ python scripts/extract_pe.py tests/data/dntojscript.bin -v
INFO:__main__:record 32: found array
INFO:__main__:record 32: found byte array
INFO:__main__:record 32: found PE byte array
INFO:__main__:writing PE to cd040cc16144ff4a91b333f3f0cb06ca.bin
```


### show_structure.py

Parse the serialized data and show its structure in a tree-like format.

Example::

```
00000000 (6418) SerializedData: SerializedData
00000000 (17)   0: SerializationHeaderRecord
00000000 (01)     RecordTypeEnum: SerializedStreamHeader (0x00000000)
00000001 (04)     RootId: 0x00000001 (1)
00000005 (04)     HeaderId: 0xffffffff (4294967295)
00000009 (04)     MajorVersion: 0x00000001 (1)
0000000d (04)     MinorVersion: 0x00000000 (0)
00000011 (204)   1: SystemClassWithMembersAndTypes
00000011 (01)     RecordTypeEnum: SystemClassWithMembersAndTypes (0x00000004)
00000012 (68)     ClassInfo: ClassInfo
00000012 (04)       ObjectId: 0x00000001 (1)
00000016 (35)       Name: LengthPrefixedString: System.DelegateSerializationHolder
00000039 (04)       MemberCount: 0x00000003 (3)
0000003d (25)       MemberNames: VArray
0000003d (09)         0: LengthPrefixedString: Delegate
00000046 (08)         1: LengthPrefixedString: target0
0000004e (08)         2: LengthPrefixedString: method0
00000056 (135)     MemberTypeInfo: MemberTypeInfo
00000056 (03)       BinaryTypeEnums: VArray
00000056 (01)         0: SystemClass (0x00000003)
00000057 (01)         1: SystemClass (0x00000003)
00000058 (01)         2: SystemClass (0x00000003)
00000059 (132)       AdditionalInfos: VArray
00000059 (49)         0: LengthPrefixedString: System.DelegateSerializationHolder+DelegateEntry
0000008a (35)         1: LengthPrefixedString: System.DelegateSerializationHolder
000000ad (48)         2: LengthPrefixedString: System.Reflection.MemberInfoSerializationHolder
000000dd (05)   2: MemberReference
000000dd (01)     RecordTypeEnum: MemberReference (0x00000009)
000000de (04)     IdRef: 0x00000002 (2)
000000e2 (05)   3: MemberReference
000000e2 (01)     RecordTypeEnum: MemberReference (0x00000009)
000000e3 (04)     IdRef: 0x00000003 (3)
000000e7 (05)   4: MemberReference
000000e7 (01)     RecordTypeEnum: MemberReference (0x00000009)
000000e8 (04)     IdRef: 0x00000004 (4)
000000ec (194)   5: SystemClassWithMembersAndTypes
000000ec (01)     RecordTypeEnum: SystemClassWithMembersAndTypes (0x00000004)
000000ed (137)     ClassInfo: ClassInfo
000000ed (04)       ObjectId: 0x00000002 (2)
000000f1 (49)       Name: LengthPrefixedString: System.DelegateSerializationHolder+DelegateEntry
00000122 (04)       MemberCount: 0x00000007 (7)
00000126 (80)       MemberNames: VArray
00000126 (05)         0: LengthPrefixedString: type
0000012b (09)         1: LengthPrefixedString: assembly
00000134 (07)         2: LengthPrefixedString: target
0000013b (19)         3: LengthPrefixedString: targetTypeAssembly
0000014e (15)         4: LengthPrefixedString: targetTypeName
0000015d (11)         5: LengthPrefixedString: methodName
00000168 (14)         6: LengthPrefixedString: delegateEntry
00000176 (56)     MemberTypeInfo: MemberTypeInfo
00000176 (07)       BinaryTypeEnums: VArray
00000176 (01)         0: String (0x00000001)
00000177 (01)         1: String (0x00000001)
00000178 (01)         2: Object (0x00000002)
00000179 (01)         3: String (0x00000001)
0000017a (01)         4: String (0x00000001)
0000017b (01)         5: String (0x00000001)
0000017c (01)         6: SystemClass (0x00000003)
0000017d (49)       AdditionalInfos: VArray
0000017d (49)         0: LengthPrefixedString: System.DelegateSerializationHolder+DelegateEntry
000001ae (53)   6: BinaryObjectString
000001ae (01)     RecordTypeEnum: BinaryObjectString (0x00000006)
000001af (04)     ObjectId: 0x00000005 (5)
000001b3 (48)     Value: LengthPrefixedString: System.Runtime.Remoting.Messaging.HeaderHandler
000001e3 (81)   7: BinaryObjectString
000001e3 (01)     RecordTypeEnum: BinaryObjectString (0x00000006)
000001e4 (04)     ObjectId: 0x00000006 (6)
000001e8 (76)     Value: LengthPrefixedString: mscorlib, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
00000234 (13)   8: BinaryObjectString
00000234 (01)     RecordTypeEnum: BinaryObjectString (0x00000006)
00000235 (04)     ObjectId: 0x00000007 (7)
00000239 (08)     Value: LengthPrefixedString: target0
00000241 (05)   9: MemberReference
00000241 (01)     RecordTypeEnum: MemberReference (0x00000009)
00000242 (04)     IdRef: 0x00000006 (6)
00000246 (21)   10: BinaryObjectString
00000246 (01)     RecordTypeEnum: BinaryObjectString (0x00000006)
00000247 (04)     ObjectId: 0x00000009 (9)
0000024b (16)     Value: LengthPrefixedString: System.Delegate
0000025b (19)   11: BinaryObjectString
0000025b (01)     RecordTypeEnum: BinaryObjectString (0x00000006)
0000025c (04)     ObjectId: 0x0000000a (10)
00000260 (14)     Value: LengthPrefixedString: DynamicInvoke
0000026e (01)   12: ObjectNull
0000026e (01)     RecordTypeEnum: ObjectNull (0x0000000a)
0000026f (170)   13: SystemClassWithMembersAndTypes
0000026f (01)     RecordTypeEnum: SystemClassWithMembersAndTypes (0x00000004)
00000270 (68)     ClassInfo: ClassInfo
00000270 (04)       ObjectId: 0x00000003 (3)
00000274 (35)       Name: LengthPrefixedString: System.DelegateSerializationHolder
00000297 (04)       MemberCount: 0x00000003 (3)
0000029b (25)       MemberNames: VArray
0000029b (09)         0: LengthPrefixedString: Delegate
000002a4 (08)         1: LengthPrefixedString: target0
000002ac (08)         2: LengthPrefixedString: method0
000002b4 (101)     MemberTypeInfo: MemberTypeInfo
000002b4 (03)       BinaryTypeEnums: VArray
000002b4 (01)         0: SystemClass (0x00000003)
000002b5 (01)         1: PrimitiveArray (0x00000007)
000002b6 (01)         2: SystemClass (0x00000003)
000002b7 (98)       AdditionalInfos: VArray
000002b7 (49)         0: LengthPrefixedString: System.DelegateSerializationHolder+DelegateEntry
000002e8 (01)         1: Byte (0x00000002)
000002e9 (48)         2: LengthPrefixedString: System.Reflection.MemberInfoSerializationHolder
00000319 (05)   14: MemberReference
00000319 (01)     RecordTypeEnum: MemberReference (0x00000009)
0000031a (04)     IdRef: 0x0000000b (11)
0000031e (05)   15: MemberReference
0000031e (01)     RecordTypeEnum: MemberReference (0x00000009)
0000031f (04)     IdRef: 0x0000000c (12)
00000323 (05)   16: MemberReference
00000323 (01)     RecordTypeEnum: MemberReference (0x00000009)
00000324 (04)     IdRef: 0x0000000d (13)
00000328 (144)   17: SystemClassWithMembersAndTypes
00000328 (01)     RecordTypeEnum: SystemClassWithMembersAndTypes (0x00000004)
00000329 (122)     ClassInfo: ClassInfo
00000329 (04)       ObjectId: 0x00000004 (4)
0000032d (48)       Name: LengthPrefixedString: System.Reflection.MemberInfoSerializationHolder
0000035d (04)       MemberCount: 0x00000006 (6)
00000361 (66)       MemberNames: VArray
00000361 (05)         0: LengthPrefixedString: Name
00000366 (13)         1: LengthPrefixedString: AssemblyName
00000373 (10)         2: LengthPrefixedString: ClassName
0000037d (10)         3: LengthPrefixedString: Signature
00000387 (11)         4: LengthPrefixedString: MemberType
00000392 (17)         5: LengthPrefixedString: GenericArguments
000003a3 (21)     MemberTypeInfo: MemberTypeInfo
000003a3 (06)       BinaryTypeEnums: VArray
000003a3 (01)         0: String (0x00000001)
000003a4 (01)         1: String (0x00000001)
000003a5 (01)         2: String (0x00000001)
000003a6 (01)         3: String (0x00000001)
000003a7 (01)         4: Primitive (0x00000000)
000003a8 (01)         5: SystemClass (0x00000003)
000003a9 (15)       AdditionalInfos: VArray
000003a9 (01)         0: Int32 (0x00000008)
000003aa (14)         1: LengthPrefixedString: System.Type[]
000003b8 (05)   18: MemberReference
000003b8 (01)     RecordTypeEnum: MemberReference (0x00000009)
000003b9 (04)     IdRef: 0x0000000a (10)
000003bd (05)   19: MemberReference
000003bd (01)     RecordTypeEnum: MemberReference (0x00000009)
000003be (04)     IdRef: 0x00000006 (6)
000003c2 (05)   20: MemberReference
000003c2 (01)     RecordTypeEnum: MemberReference (0x00000009)
000003c3 (04)     IdRef: 0x00000009 (9)
000003c7 (50)   21: BinaryObjectString
000003c7 (01)     RecordTypeEnum: BinaryObjectString (0x00000006)
000003c8 (04)     ObjectId: 0x00000011 (17)
000003cc (45)     Value: LengthPrefixedString: System.Object DynamicInvoke(System.Object[])
000003f9 (04)   22: MemberPrimitiveTyped
000003f9 (01)     RecordTypeEnum: MemberPrimitiveTyped (0x00000008)
000003fa (01)     PrimitiveTypeEnum: 0 (0x00000000)
000003fb (02)     Value: 0x00000000 (0)
000003fd (00)     _eof: 
000003fd (01)   23: ObjectNull
000003fd (01)     RecordTypeEnum: ObjectNull (0x0000000a)
000003fe (09)   24: ClassWithId
000003fe (01)     RecordTypeEnum: ClassWithId (0x00000001)
000003ff (04)     ObjectId: 0x0000000b (11)
00000403 (04)     MetadataId: 0x00000002 (2)
00000407 (38)   25: BinaryObjectString
00000407 (01)     RecordTypeEnum: BinaryObjectString (0x00000006)
00000408 (04)     ObjectId: 0x00000012 (18)
0000040c (33)     Value: LengthPrefixedString: System.Xml.Schema.XmlValueGetter
0000042d (83)   26: BinaryObjectString
0000042d (01)     RecordTypeEnum: BinaryObjectString (0x00000006)
0000042e (04)     ObjectId: 0x00000013 (19)
00000432 (78)     Value: LengthPrefixedString: System.Xml, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
00000480 (13)   27: BinaryObjectString
00000480 (01)     RecordTypeEnum: BinaryObjectString (0x00000006)
00000481 (04)     ObjectId: 0x00000014 (20)
00000485 (08)     Value: LengthPrefixedString: target0
0000048d (05)   28: MemberReference
0000048d (01)     RecordTypeEnum: MemberReference (0x00000009)
0000048e (04)     IdRef: 0x00000006 (6)
00000492 (32)   29: BinaryObjectString
00000492 (01)     RecordTypeEnum: BinaryObjectString (0x00000006)
00000493 (04)     ObjectId: 0x00000016 (22)
00000497 (27)     Value: LengthPrefixedString: System.Reflection.Assembly
000004b2 (10)   30: BinaryObjectString
000004b2 (01)     RecordTypeEnum: BinaryObjectString (0x00000006)
000004b3 (04)     ObjectId: 0x00000017 (23)
000004b7 (05)     Value: LengthPrefixedString: Load
000004bc (01)   31: ObjectNull
000004bc (01)     RecordTypeEnum: ObjectNull (0x0000000a)
000004bd (5130)   32: ArraySinglePrimitive
000004bd (01)     RecordTypeEnum: ArraySinglePrimitive (0x0000000f)
000004be (08)     ArrayInfo: ArrayInfo
000004be (04)       ObjectId: 0x0000000c (12)
000004c2 (04)       Length: 0x00001400 (5120)
000004c6 (01)     PrimitiveTypeEnum: Byte (0x00000002)
000004c7 (5120)     Value: 4d5a90000300000004000000ffff0000b80000000000000040...
000018c7 (00)     _eof: 
000018c7 (09)   33: ClassWithId
000018c7 (01)     RecordTypeEnum: ClassWithId (0x00000001)
000018c8 (04)     ObjectId: 0x0000000d (13)
000018cc (04)     MetadataId: 0x00000004 (4)
000018d0 (05)   34: MemberReference
000018d0 (01)     RecordTypeEnum: MemberReference (0x00000009)
000018d1 (04)     IdRef: 0x00000017 (23)
000018d5 (05)   35: MemberReference
000018d5 (01)     RecordTypeEnum: MemberReference (0x00000009)
000018d6 (04)     IdRef: 0x00000006 (6)
000018da (05)   36: MemberReference
000018da (01)     RecordTypeEnum: MemberReference (0x00000009)
000018db (04)     IdRef: 0x00000016 (22)
000018df (45)   37: BinaryObjectString
000018df (01)     RecordTypeEnum: BinaryObjectString (0x00000006)
000018e0 (04)     ObjectId: 0x0000001a (26)
000018e4 (40)     Value: LengthPrefixedString: System.Reflection.Assembly Load(Byte[])
0000190c (04)   38: MemberPrimitiveTyped
0000190c (01)     RecordTypeEnum: MemberPrimitiveTyped (0x00000008)
0000190d (01)     PrimitiveTypeEnum: 0 (0x00000000)
0000190e (02)     Value: 0x00000000 (0)
00001910 (00)     _eof: 
00001910 (01)   39: ObjectNull
00001910 (01)     RecordTypeEnum: ObjectNull (0x0000000a)
00001911 (01)   40: MessageEnd
00001911 (01)     RecordTypeEnum: MessageEnd (0x0000000b)
```
